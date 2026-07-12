// 65. Create a CourseCard.jsx component that accepts name, code, credits, and 
// grade as props and renders a styled card.

function CourseCard(props) {
    return (
        <article className="course-card">

            <h3>{props.name}</h3>

            <p>
                <strong>Code:</strong> {props.code}
            </p>

            <p>
                <strong>Credits:</strong> {props.credits}
            </p>

            <p>
                <strong>Grade:</strong> {props.grade}
            </p>

            <button onClick={() => props.onEnroll(props)}>
                Enroll
            </button>
            
        </article>
    );
}

export default CourseCard;