import { context } from "@/components/admin/enums"
import axios, { AxiosResponse } from "axios"

export interface UserType{
    user_id: string
    email: string
    password: string
    user_name: string
    token: string
    create_at: string
    updated_at: string
}
export const userJoinApi = async (
    payload: {
    user_id: string
    email: string
    password: string
    user_name: string
    token: string
    create_at: string
    updated_at: string}) => {
    const headers = context.headers    
    try{
        const response : AxiosResponse<unknown, UserType[]> = await axios.post(`${context.server}/users`, payload, {headers})
    }catch(error){
        console.log(``)
    }
}