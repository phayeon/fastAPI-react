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

const userSlice = createSlice({
    name: 'userSlice',
    initialState,
    reducers: {
        joinRequest(state: IUserState, _payload){
            state.status = 'loading'
        },
        joinSuccess(state: IUserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        joinFailed(state: IUserState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        },
        loginRequest(state: IUserState, _payload){
            state.status = 'loading'
        },
        loginSuccess(state: IUserState, {payload}){
            state.status = 'idle'
            state.data = [...state.data, payload]
        },
        loginFailed(state: IUserState, {payload}){
            state.status = 'failed'
            state.data = [...state.data, payload]
        }
    }
})

export const {joinRequest, joinSuccess, joinFailed,
    loginRequest, loginSuccess, loginFailed
} = userSlice.actions
export default userSlice