import axios from 'axios';
import { useState, useEffect } from 'react';

export default function Home(){
    const [list, setList] = useState([])
    const [rowCnt, setRowCnt] = useState(0)
    const [requestPage, setRequestPage] = useState(0)
    const [startRowPerPage, setStartRowPerPage] = useState(0)
    const [endRowPerPage, setEndRowPerPage] = useState(0)
    const [startPagePerBlock, setStartPagePerBlock] = useState(0)
    const [endPagePerBlock, setEndPagePerBlock] = useState(0)
    const [rows, setRows] = useState<number[]>([])
    const [pages, setPages] = useState<number[]>([])
    const [prevArrow, setPrevArrow] = useState(false)
    const [nextArrow, setNextArrow] = useState(false)

    useEffect(()=>{
        axios
        .get('http://localhost:8000/users/page/11')
        .then(res => {
            setRowCnt(Number(res.data.pager.row_cnt))
            setStartRowPerPage(Number(res.data.pager.start_row_per_page))
            setEndRowPerPage(Number(res.data.pager.end_row_per_page))
            setStartPagePerBlock(Number(res.data.pager.start_page_per_block))
            setEndPagePerBlock(Number(res.data.pager.end_page_per_block))
            setRequestPage(Number(res.data.pager.request_page))
            alert(` 사용자가 요청한 페이지 번호: ${requestPage}`)
            console.log(` 사용자가 요청한 페이지 번호: ${requestPage}`)
            console.log(` 페이지 시작 행번호: ${startRowPerPage}`)
            console.log(` 페이지 마지막 행번호: ${endRowPerPage}`)
            console.log(` 블록 시작 페이지번호: ${startPagePerBlock}`)
            console.log(` 블록 마지막 페이지번호: ${endPagePerBlock}`)
            setList(res.data.users.items)
            console.log(" ### 페이지 내용 표시 ### ")
            let rows:number[] = []
            let pages:number[] = []
            for(let i =startRowPerPage; i <= endRowPerPage; i++){
                console.log(`page index : ${i}`)
                rows.push(i)
            }
            setRows(rows)
            console.log(" ### 블록 내용 표시 ### ")
            for(let i =startPagePerBlock; i <= endPagePerBlock; i++){
              console.log(`block index : ${i}`)
              pages.push(i)
           }
           setPages(pages)
           setPrevArrow(res.data.pager.prevArrow)
           setNextArrow(res.data.pager.nextArrow)
        })
        .catch(err => {console.log(err)})
    }, [])

    return (<>
        <h2>회원목록</h2>
        <h6>회원 수: {rowCnt}</h6>
        <h6></h6>
        <h6></h6>
        <h6></h6>
        <table className='user-list'>
            <thead>
                <tr>
                <th>ID</th><th>이메일</th><th>비밀번호</th><th>이름</th>
                </tr>
            </thead>
            {prevArrow && <span> ← </span>}
            <tbody>
            {list && list.map(({user_id, email, password, user_name})=>(
                <tr key={user_id}>
                    <td>{user_id}</td><td>{email}</td><td>{password}</td><td>{user_name}</td>
                </tr>
            ))}
            {nextArrow && <span> → </span>}
            </tbody>
        </table>
        <div>
            {pages && pages.map((v, i) => (<span style={{"border": "1px solid black"}} >{v+1}</span>))}
        </div>
        <div className="container">
        <h1>React TypeScript Pagination</h1>
        </div>
    </>)
}

