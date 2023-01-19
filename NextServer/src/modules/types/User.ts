export interface User{
    user_id?: string,
    email?: string,
    password?: string,
    cpassword?: string,
    user_name?: string,
    token?: string,
    create_at?: string,
    updated_at?: string
}

export interface UserLoginInput{
    email: string,
    password: string
}