// 76. Wrap your <App /> in <BrowserRouter> in main.jsx.

// 77. Define routes in App.jsx using <Routes> and <Route>: 
// / → HomePage, /courses → CoursesPage, /profile → ProfilePage, /courses/:courseId → CourseDetailPage.

// 78. Update the Header nav links to use React Router's <Link> component instead of <a> tags.

// 79. In CourseDetailPage.jsx, use the useParams() hook to read the courseId from the URL and display the matching course details.

// 80. Add a useNavigate() hook: after clicking Enroll on a course, navigate the user to /profile automatically.

// 81. Create EnrollmentContext.jsx: define a context with createContext(), 
// a provider component that holds enrolledCourses state, and exports both.

// 82. Wrap the app in <EnrollmentProvider> in main.jsx.

// 83. In any component that needs enrolled courses (e.g., Header for count, ProfilePage for list), 
// consume the context using useContext(EnrollmentContext) instead of receiving props.

// 84. Add a Remove function to the context: allow students to un-enroll from a course from the ProfilePage.

// 85. Verify that enrolling on the CoursesPage and viewing the count in the Header both reflect the same state — 
// without any props being passed between them.

// 86. Create store.js using configureStore from @reduxjs/toolkit.

// 87. Create enrollmentSlice.js using createSlice with initial state { enrolledCourses: [] } and two reducers: 
// enroll(state, action) and unenroll(state, action).

// 88. Replace the Context-based enrollment state with Redux: 
// dispatch the enroll action on Enroll click, dispatch unenroll on Remove.

// 89. Read state in components using useSelector(state => state.enrollment.enrolledCourses).

// 90. Open Redux DevTools in the browser. Enroll and un-enroll a course and observe the action log and state diff.