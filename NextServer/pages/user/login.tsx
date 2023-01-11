import { NextPage } from "next"
import GoogleLogin from "@/components/user/GoogleLogin"
import Login from "@/components/user/Login"


const LoginPage: NextPage = function(){

    return (
        <>
           <Login/>
           <GoogleLogin/>
        </>
            
        
 );
}
export default LoginPage