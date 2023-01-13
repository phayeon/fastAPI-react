

export default function GoogleLogin(){

    return (
        <>
            <h1>구글로그인</h1>
            <form action="/send-data-here" method="post" >
                <label htmlFor="email">User Email:</label>
                <input type="text"  id="email" name="email" required minLength= {10} maxLength={20}/>
                <label htmlFor="password">Password:</label>
                <input type="text" id="password" name="password" required />
                <button type="submit">Submit</button>
            </form> 
        </>
            
        
 );
}
