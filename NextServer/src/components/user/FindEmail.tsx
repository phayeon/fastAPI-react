
export default function FindEmail(){

    return (
        <>
            <h1>이메일 찾기</h1>
            <form action="/send-data-here">
                <label htmlFor="user_name">user_name:</label>
                <input type="text" id="user_name" name="user_name" required />
                <label htmlFor="phone">password:</label>
                <input type="text" id="password" name="password" required />
                <button type="submit">Submit</button>
            </form> 
        </>
            
        
 );
}
