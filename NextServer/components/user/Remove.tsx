export default function UserRemove(){
    
    return (<>
    <h1>회원탈퇴</h1>
    <form action="/send-data-here">
    <label htmlFor="user_email">비밀번호 확인:</label>
    <input type="text"  id="password" name="password" required/>
    <button type="submit">Submit</button>
    </form> 
    </>)
}
