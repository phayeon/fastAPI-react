import { configureStore, AnyAction, CombinedState, combineReducers } from '@reduxjs/toolkit'
import { createWrapper } from 'next-redux-wrapper'
import logger from 'redux-logger'
import createSagaMiddleware from "@redux-saga/core"
import reducer from '@/modules/counter/counterSlice'

const sagaMiddleware = createSagaMiddleware()

const isDev = process.env.NODE_ENV === 'development'

const makestore = () =>
    configureStore({
        reducer,
        middleware: getDefaultMiddleware =>
            isDev ? getDefaultMiddleware().concat(logger) : getDefaultMiddleware(),
        devTools: isDev
    });

export const wrapper = createWrapper(makestore, {
    debug: isDev
}) ;

const store = makestore();

export type AppState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

export default store;