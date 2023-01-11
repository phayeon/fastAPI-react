export default function UserLogin(){
    
    return (
    <>
        <h1>로그인</h1>
        <form action="/send-data-here" method="post">

        <label htmlFor="email">email:</label>
        <div id="email"/>

        <label htmlFor="password">password:</label>
        <div id="password"/>
        
        <button type="submit">Submit</button>
        </form>
    </>)
}
