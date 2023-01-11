export default function Join() {
    const validateFormWithJS = () => {
        // const name = document.querySelector('#name').value
        // const rollNumber = document.querySelector('#rollNumber').value
        const name = ""
        const rollNumber = ""
    
        if (!name) {
          alert('Please enter your name.')
          return false
        }
    
        if (rollNumber.length < 3) {
          alert('Roll Number should be at least 3 digits long.')
          return false
        }
      }

    return (<>
        <h2>회원가입</h2>
        <button >사용자 등록</button>
        <p>버튼을 클릭하시면, 더미 사용자 100명이 등록됩니다.</p>

        <form action="/send-data-here" method="post">

        <label htmlFor="email">email : </label>
        <input type="text" id="email" name="email" required minLength={4} maxLength={20}/><br/>

        <label htmlFor="password">password : </label>
        <input type="text" id="password" name="password" required minLength={4} maxLength={20}/><br/>

        <label htmlFor="user_name">user_name : </label>
        <input type="text" id="user_name" name="user_name" required/><br/>

        <button type="submit">Submit</button>
        </form>
        </>)
}
