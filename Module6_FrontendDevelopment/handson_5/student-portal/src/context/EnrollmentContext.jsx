// 81. Create EnrollmentContext.jsx: define a context with createContext(), 
// a provider component that holds enrolledCourses state, and exports both.

import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

export function EnrollmentProvider({ children }) {

    const [enrolledCourses, setEnrolledCourses] = useState([]);
    
    function enrollCourse(course) {
        const alreadyEnrolled = enrolledCourses.some(
            enrolledCourse => enrolledCourse.id === course.id
        );

        if (!alreadyEnrolled) {
            setEnrolledCourses([
                ...enrolledCourses,
                course
            ]);
        }
    }

    // 84. Add a Remove function to the context: 
    // allow students to un-enroll from a course from the ProfilePage.
    function removeCourse(courseId) {
        setEnrolledCourses(
            enrolledCourses.filter(
                course => course.id !== courseId
            )
        );
    }

    return (
        <EnrollmentContext.Provider
            value={{
                enrolledCourses,
                setEnrolledCourses
            }}
        >
            {children}
        </EnrollmentContext.Provider>

    );

}