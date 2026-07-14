import { useContext } from "react";
import { EnrollmentContext } from "../context/EnrollmentContext";

function ProfilePage() {
    // 83. In any component that needs enrolled courses (e.g., Header for count, ProfilePage for list), 
    // consume the context using useContext(EnrollmentContext) instead of receiving props.
    const { enrolledCourses } = useContext(EnrollmentContext);

    return (
        <section>
            <h2>My Enrolled Courses</h2>
            {
                enrolledCourses.length === 0 ? (<p>No courses enrolled.</p>) : (
                    <ul>
                        {
                            enrolledCourses.map(course => (
                                <li key={course.id}> {course.name} ({course.code}) </li>
                            ))
                        }
                    </ul>
                )
            }
        </section>
    );
}

export default ProfilePage;