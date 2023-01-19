export interface Article{
    art_seq? : number
    title? : string
    content? : string
    create_at? : string
    updated_at? : string
    user_id? : string
}

export interface InputImage{
    name: string
    lastModified: number
    lastModifiedDate: number
    type: string
    webkitRelativePath: string    
    size : number
}


export interface ImageState{
    data: InputImage
    status: 'successed' | 'loading' | 'failed'
}

export interface UploadFileResponse {
    success: boolean,
    message: string
}
export interface GetFileResponse {
    success: boolean,
    message: string
}

export interface ValidatorResponse {
    isValid: boolean,
    errorMessage: string
}

export const fileTypes = [
    'jpg',
    'png',
    'mp3',
    'mp4',
    'gif'

]