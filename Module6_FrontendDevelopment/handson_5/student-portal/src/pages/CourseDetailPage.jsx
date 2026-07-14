// 79. In CourseDetailPage.jsx, use the useParams() hook to read the courseId from the URL and display the matching course details.
import { useParams } from "react-router-dom";
import { courseData } from "../data";

function CourseDetailPage() {
    const { courseId } = useParams();

    const course = courseData.find(
        course => course.id === Number(courseId)
    );

    if (!course) {
        return <h2>Course not found</h2>;
    }

    return (
        <section>
            <h2>{course.name}</h2>
            <p> <strong>Course Code:</strong> {course.code} </p>
            <p> <strong>Credits:</strong> {course.credits} </p>
            <p> <strong>Grade:</strong> {course.grade} </p>
        </section>
    );
}

export default CourseDetailPage;