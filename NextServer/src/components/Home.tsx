import axios from 'axios';
import { useState, useEffect } from 'react';
import Pagination from './pagination';

export default function Home(){
    const [currentPage, setCurrentPage] = useState(1);
    const lastPage = 3;
    const [list, setList] = useState([])
    const [count, setCount] = useState(0)
    useEffect(()=>{
        axios
        .get('http://localhost:8000/users/page/1')
        .then(res => {
            const items = res.data.pager.items
            setCount(count)
            setList(items)
        })
        .catch(err => {console.log(err)})
    }, [])
    return (<>
        <h2>회원목록 총 {count}명</h2>
        <table className='user-list'>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>비밀번호</th><th>이름</th>
                </tr>
            </thead>
            <tbody>
            {list && list.map(({user_id, email, password, user_name})=>(
                <tr key={user_id}>
                    <td>{user_id}</td><td>{email}</td><td>{password}</td><td>{user_name}</td>
                </tr>
            ))}
            </tbody>
        </table>
        <div className="container">
        <h1>React TypeScript Pagination</h1>
        <Pagination
            currentPage={currentPage}
            lastPage={lastPage}
            maxLength={7}
            setCurrentPage={setCurrentPage}
        />
        </div>
    </>)
}

