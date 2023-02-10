from starlette.responses import JSONResponse
from app.schemas.kakao_chat import ChatDTO
from app.crud.kakao_caht import KakaoChatCrud
from typing import List
from fastapi import WebSocket, APIRouter
from fastapi.responses import HTMLResponse
from starlette.websockets import WebSocketDisconnect

from app.services.food_intent.models.intent.model_test import ModelTest

router = APIRouter()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/chatbot/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.get("")
async def get():
    return HTMLResponse(html)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"You wrote: {data}", websocket)
            answer = ModelTest().test()
            await manager.broadcast(f"Client # says: {answer}")
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client # left the chat")


@router.post("/create-sentence", status_code=201)
async def create_sentence(data: ChatDTO):
    print(f'포스트 맨에서 받은 문장: {data.sentence}')
    return JSONResponse(status_code=200,
                        content=dict(
                            msg=KakaoChatCrud(request_sentence=data.sentence).create_sentence()))
