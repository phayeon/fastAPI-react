import { all, fork } from "redux-saga/effects"
import{
    watchJoin
} from "./userSaga"

export default function* rootStage(){
    yield all([
        fork(watchJoin)
    ])
}