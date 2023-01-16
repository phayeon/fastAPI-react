import { NextPage } from "next"
import { useEffect, useState } from "react"
interface Props{ user: string }
const LoginHomePage: NextPage<Props> = () => {
    const [email, setemail] = useState("")
    useEffect(()=>{
        setemail(JSON.stringify(localStorage.getItem("data")))
    }
    )
    return (<><div>{email}님 반갑습니다.</div></>)
}
export default LoginHomePage