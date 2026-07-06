// 30. In app.js, import the array using ES6 import. Use destructuring to extract 
// name and credits from each course in a loop.
import { courses } from './data.js';

courses.forEach(({ name, credits }) => {
    console.log(name, credits);
});


// 31. Use Array.map() to create a new array of strings formatted as 
// 'CS101 — Data Structures (4 credits)'. Log the result.
const formattedCourses = courses.map(
    ({ code, name, credits }) =>
        `${code} — ${name} (${credits} credits)`
);

console.log(formattedCourses);


// 32. Use Array.filter() to get only courses with credits >= 4. Log the count.
const highCreditCourses =
    courses.filter(course => course.credits >= 4);

console.log(
    "Courses with >=4 credits:",
    highCreditCourses.length
);


// 33. Use Array.reduce() to calculate the total credits enrolled. Log the result.
const totalCredits =
    courses.reduce(
        (sum, course) => sum + course.credits,
        0
    );

console.log("Total Credits:", totalCredits);


// 36. In app.js, use document.querySelector('.course-grid') to select the grid container.
const courseGrid =
    document.querySelector(".course-grid");

const totalCreditsText =
    document.querySelector("#total-credits");

const searchInput =
    document.querySelector("#search-courses");

const sortButton =
    document.querySelector("#sort-btn");

const selectedCourse =
    document.querySelector("#selected-course");


// 37. Loop through your course data array. For each course, create a <article> element using document.createElement(), 
// set its className, and build its inner HTML using a template literal with course name, code, and credits.
function renderCourses(courseList) {

    courseGrid.innerHTML = "";

    courseList.forEach(course => {

        const article =
            document.createElement("article");

        article.className = "course-card";

        article.dataset.id = course.id;

        article.innerHTML = `
            <h3>${course.name}</h3>
            <p><strong>Code:</strong> ${course.code}</p>
            <p><strong>Credits:</strong> ${course.credits}</p>
        `;

        // 38. Append each created article to the course grid using appendChild().
        courseGrid.appendChild(article);

    });

    // 39. Add a <p id='total-credits'> below the grid. After rendering, 
    // update its textContent to display the total credits dynamically.
    totalCreditsText.textContent =
        `Total Credits: ${courseList.reduce(
            (sum, course) => sum + course.credits,
            0
        )}`;
}

/* ===========================
   Initial Render
=========================== */

renderCourses(courses);

// 41. Add an event listener on the input's 'input' event. On each keystroke, 
// filter the course array by name (case-insensitive) and re-render only the matching cards.
searchInput.addEventListener("input", event => {

    const keyword =
        event.target.value.toLowerCase();

    const filteredCourses =
        courses.filter(course =>
            course.name
                .toLowerCase()
                .includes(keyword)
        );

    renderCourses(filteredCourses);

});


sortButton.addEventListener("click", () => {

    const sortedCourses =
        [...courses].sort(
            (a, b) => b.credits - a.credits
        );

    renderCourses(sortedCourses);

});


// 43. Add a click event to each course card: when clicked, display an alert 
// (or update a <div id='selected course'>) showing the course name and grade.
// ...
// 44. Use event delegation: attach a single click listener to the course-grid container 
// and detect which card was clicked using event.target.closest('.course-card').
courseGrid.addEventListener("click", event => {

    const card =
        event.target.closest(".course-card");

    if (!card) return;

    const id =
        Number(card.dataset.id);

    const course =
        courses.find(c => c.id === id);

    selectedCourse.textContent =
        `Selected Course: ${course.name} | Grade: ${course.grade}`;

});