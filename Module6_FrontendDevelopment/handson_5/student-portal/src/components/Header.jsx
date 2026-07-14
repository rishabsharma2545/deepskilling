// 62. Create Header.jsx — a functional component that renders the site title and a nav bar with links (Home, Courses, Profile).

import { Link } from "react-router-dom";

import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function Header(props) {

    // 83. In any component that needs enrolled courses (e.g., Header for count, ProfilePage for list), 
    // consume the context using useContext(EnrollmentContext) instead of receiving props.
    const { enrolledCourses } = useContext(EnrollmentContext);
    
    return (
        <header>
            <h1>{props.siteName}</h1>

            <nav>
                <ul>
                    {/* 
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Courses</a></li>
                    <li><a href="#">Profile</a></li> 
                    
                    78. Update the Header nav links to use React Router's <Link> component instead of <a> tags.*/}
                    <li><Link to="/">Home</Link></li>
                    <li><Link to="/courses">Courses</Link></li>
                    <li><Link to="/profile">Profile</Link></li>
                </ul>
            </nav>

            <p>
                Enrolled Courses: {enrolledCourses.length}
            </p>
            
        </header>
    );
}

export default Header;