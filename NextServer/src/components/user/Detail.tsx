export default function UserDetail() {

    return (<>
        <h2>회원정보</h2>
        <div>

          <label htmlFor="email">Email :</label>
          <div id="email" ></div>

          <label htmlFor="password">Password : </label>
          <div id="password" ></div>

          <label htmlFor="user_name">user_name:</label>
          <div id="user_name" ></div>

          <button>수정하기</button>
          </div> 
        </>)
}
