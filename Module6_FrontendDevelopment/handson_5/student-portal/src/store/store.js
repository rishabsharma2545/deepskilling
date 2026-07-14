// 86. Create store.js using configureStore from @reduxjs/toolkit.

import { configureStore } from "@reduxjs/toolkit";
import enrollmentReducer from "./enrollmentSlice";

const store = configureStore({
    reducer: {
        enrollment: enrollmentReducer
    }
});

export default store;