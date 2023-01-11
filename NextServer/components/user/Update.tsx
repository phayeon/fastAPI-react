export default function UserUpdate(){
    
  return (
  <>
    <h1>회원정보 수정</h1>
    <form action="/send-data-here" method="put">

    <label htmlFor="email">email:</label>
    <div id="email"/>

    <label htmlFor="password">password:</label>
    <div id="password"/>

    <label htmlFor="user_name">user_name:</label>
    <div id="user_name"/>
    
    <button type="submit">Submit</button>
    </form>
  </>)
}
