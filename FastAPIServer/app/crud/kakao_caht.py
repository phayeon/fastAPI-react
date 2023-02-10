from abc import ABC
from app.bases.kakao_chat import ChatBase
from app.services.kakao_chat.kakao_chat import KakaoChatbot


class KakaoChatCrud(ChatBase, ABC):
    def __init__(self, request_sentence):
        self.prompt = request_sentence

    def create_sentence(self) -> str:
        prompt = self.prompt
        return KakaoChatbot().exec_1(prompt)

    def sentence_classification(self) -> str:
        prompt = self.prompt
        return KakaoChatbot().exec_2(prompt)

    def sentence_summary(self) -> str:
        prompt = self.prompt
        return KakaoChatbot().exec_3(prompt)

    def short_answer_question(self) -> str:
        prompt = self.prompt
        return KakaoChatbot().exec_4(prompt)

    def inference_of_correct_answers(self) -> str:
        prompt = self.prompt
        return KakaoChatbot().exec_5(prompt)

    def conversion_of_speech(self) -> str:
        prompt = self.prompt
        return KakaoChatbot().exec_6(prompt)

    def question_and_answer(self) -> str:
        prompt = self.prompt
        return KakaoChatbot().exec_7(prompt)
