import { useState, useEffect } from "react";

import { Routes, Route, useNavigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import CoursesPage from "./pages/CoursesPage";
import ProfilePage from "./pages/ProfilePage";
import CourseDetailPage from "./pages/CourseDetailPage";

import { courseData } from "./data";
import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

import { useContext } from "react";
import { EnrollmentContext } from "./context/EnrollmentContext";

const { enrollCourse } = useContext(EnrollmentContext);

import { useDispatch } from "react-redux";
import { enroll } from "./store/enrollmentSlice";

const dispatch = useDispatch();

// 69. Pass the handler as a prop: onEnroll={handleEnroll}.
function handleEnroll(course) {
    // const alreadyEnrolled = enrolledCourses.some(
    //     enrolledCourse => enrolledCourse.id === course.id
    // );

    // if (!alreadyEnrolled) {
    //     setEnrolledCourses([
    //         ...enrolledCourses,
    //         course
    //     ]);
    // }

    // enrollCourse(course);

    dispatch(enroll(course));

    // 80. After clicking Enroll on a course, navigate the user to /profile automatically
    navigate("/profile");
}

// 71. In App.jsx, add a useEffect that fetches courses from JSONPlaceholder /posts.
useEffect(() => {
    async function fetchCourses() {
        try {
            const response = await fetch(
                "https://jsonplaceholder.typicode.com/posts"
            );

            if (!response.ok) {
                throw new Error("Failed to fetch courses.");
            }

            const posts = await response.json();
            const courseData = posts
                .slice(0, 5)
                .map(post => ({
                    id: post.id,
                    name: post.title,
                    code: `CS${100 + post.id}`,
                    credits: 3 + (post.id % 2),
                    grade: "Not Assigned"
                }));
            setCourses(courseData);
        }
        catch (err) {
            setError(err.message);
        }
        finally {
            setLoading(false);
        }
    }
    fetchCourses();
}, []);



useEffect(() => {
    console.log("Courses updated");
}, [courses]);

function App() {
    // 66. In App.jsx, create a state variable using useState.
    // and initialise it with your 5 course objects (import from a data file).
    const [courses, setCourses] = useState([]);
    
    // 68. Add a search input above the course list. Create a state variable searchTerm. 
    // On each keystroke (onChange), update searchTerm and filter the displayed courses.
    const [searchTerm, setSearchTerm] = useState("");

    const filteredCourses = courses.filter(course =>
        course.name.toLowerCase().includes(searchTerm.toLowerCase())
    );

    // 69. Add an 'Enroll' button inside CourseCard. When clicked, add the course to a 
    // new enrolledCourses state array in App.jsx (lift state up).
    const [enrolledCourses, setEnrolledCourses] = useState([]);

    // 72. Add a loading state. Set it to false after the fetch completes. 
    // Render a 'Loading...' message while loading is true.
    const [loading, setLoading] = useState(true);

    // 73. Add an error state. Catch fetch errors and display an error message if the request fails.
    const [error, setError] = useState(null);

    // 80. Add a useNavigate() hook:
    const navigate = useNavigate();


    return (
        // 64. Import and render Header and Footer inside App.jsx. Pass the site name as a prop to Header: 
        // <Header siteName='Student Portal' />. Display it inside the component using {props.siteName}.
        <>
            <Header 
                siteName="Student Portal" 
                enrolledCount={enrolledCourses.length}    
            />

            {/* 77. Define routes in App.jsx using <Routes> and <Route>: 
            / → HomePage, /courses → CoursesPage, /profile → ProfilePage, /courses/:courseId → CourseDetailPage. */}
            <main>
                <Routes>
                    <Route
                        path="/"
                        element={<HomePage />}
                    />
                    <Route
                        path="/courses"
                        element={<CoursesPage />}
                    />
                    <Route
                        path="/profile"
                        element={<ProfilePage />}
                    />
                    <Route
                        path="/courses/:courseId"
                        element={<CourseDetailPage />}
                    />
                </Routes>
            </main>

            <Footer />
        </>
    );
}

export default App;