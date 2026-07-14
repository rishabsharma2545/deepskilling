import React from "react";
import ReactDOM from "react-dom/client";
import { BrowserRouter } from "react-router-dom";

import App from "./App.jsx";
import "./App.css";

import { EnrollmentProvider } from "./context/EnrollmentContext";

import { Provider } from "react-redux";
import store from "./store/store";

ReactDOM.createRoot(document.getElementById("root")).render(
	// 76. Wrap your <App /> in <BrowserRouter> in main.jsx.
	<React.StrictMode>
		{/* 82. Wrap the app in `EnrollmentProvider` in main.jsx. */}
		{/* <EnrollmentProvider>
            <BrowserRouter>
                <App />
            </BrowserRouter>
        </EnrollmentProvider> */}

		
		<Provider store={store}>
			<BrowserRouter>
				<App />
			</BrowserRouter>
		</Provider>

	</React.StrictMode>      
);
