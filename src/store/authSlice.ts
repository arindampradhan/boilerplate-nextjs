import { createSlice } from '@reduxjs/toolkit';
import { AppState } from './index';
import { HYDRATE } from 'next-redux-wrapper';

// Type for our state
export interface AuthState {
  authState: boolean;
}

// Initial state
const initialState: AuthState = {
  authState: false
};

export interface HyderateAction {
  payload: {
    auth: any;
  };
}

// Actual Slice
export const authSlice = createSlice({
  name: 'auth',
  initialState,
  reducers: {
    // Action to set the authentication status
    setAuthState(state, action) {
      state.authState = action.payload;
    },

    // Special reducer for hydrating the state. Special case for next-redux-wrapper
    extraReducers: {
      // @ts-ignore
      [HYDRATE]: (state: any, action: HyderateAction): any => ({
        ...state,
        ...action.payload.auth
      })
    }
  }
});

export const { setAuthState } = authSlice.actions;

export const selectAuthState = (state: AppState) => state.auth.authState;

export default authSlice.reducer;
