import { createSlice, PayloadAction } from "@reduxjs/toolkit"
export interface IUserType{
    user_id: string
    email: string
    password: string
    user_name: string
    token: string
    create_at: string
    updated_at: string
}
export interface IUserState{
    data: IUserType[]
    status: 'idle' | 'loading' | 'failed'
}

const initialState: IUserState = {
    data: [],
    status: 'idle'
}