import React, { useCallback, useState } from 'react';
import { useDispatch } from 'react-redux';
//import { modify } from 'features/user/reducer/userSlice'

import styled from 'styled-components'

export default function UpdateUser() {
    const dispatch = useDispatch()
    
  return (
    <Main>
         <h1>회원정보 수정</h1>
         <form action="/send-data-here" method="put" >

          <label htmlFor="email">User Email:</label>
          <div id="email" ></div>

          <label htmlFor="password">Password:</label>
          <input type="text" id="password" name="password" required />

          <label htmlFor="user_name">user_name:</label>
          <div id="user_name" ></div>

          <button type="submit">Submit</button>
          </form> 
    </Main>
   
  );
}
const Main = styled.div`
width: 500px;
margin: 0 auto;
text-decoration:none
text-align: center;
`