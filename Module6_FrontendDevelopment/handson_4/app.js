import { courses } from "./data.js";

courses.forEach(({ name, credits }) => {
    console.log(name, credits);
});


const formattedCourses = courses.map(
    ({ code, name, credits }) =>
        `${code} — ${name} (${credits} credits)`
);
console.log(formattedCourses);


const highCreditCourses =
    courses.filter(course => course.credits >= 4);

console.log(
    "Courses with >=4 credits:",
    highCreditCourses.length
);


const totalCredits =
    courses.reduce(
        (sum, course) => sum + course.credits,
        0
    );

console.log("Total Credits:", totalCredits);


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

        courseGrid.appendChild(article);

    });

    totalCreditsText.textContent =
        `Total Credits: ${courseList.reduce(
            (sum, course) => sum + course.credits,
            0
        )}`;
}


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



// 45. Write a function fetchUser(id) that calls fetch('https://jsonplaceholder.typicode.com/users/' + id) 
// and returns a Promise. Chain .then() to parse the JSON and log the user's name.
function fetchUserPromise(id) {
    return fetch(`https://jsonplaceholder.typicode.com/users/${id}`)
        .then(response => response.json())
        .then(user => {
            console.log("User Name:", user.name);
            return user;
        });
}
fetchUserPromise(1);


// 46. Rewrite the same function using async/await and try/catch.
async function fetchUserAsync(id) {
    try {
        const response = await fetch(`https://jsonplaceholder.typicode.com/users/${id}`);

        const user = await response.json();
        console.log("User Name:", user.name);
        return user;
    }
    catch (error) {
        console.error("Error fetching user:", error);
    }
}
fetchUserAsync(1);


// 47. Write a function fetchAllCourses() that simulates a 1-second network delay using 
// new Promise(resolve => setTimeout(resolve, 1000)) and then returns your local course array.
function fetchAllCourses() {
    return new Promise(resolve => {
        setTimeout(() => {
            resolve(courses);
        }, 1000);
    });
}


// 48. Call fetchAllCourses() and render the course cards only after the promise resolves. 
// Show a 'Loading courses...' message while waiting.
const loadingMessage = document.querySelector("#loading-message");

loadingMessage.style.display = "block";
fetchAllCourses()
    .then(courseList => {
        loadingMessage.style.display = "none";
        renderCourses(courseList);
    });


// 49. Demonstrate Promise.all(): fetch user ID 1 and user ID 2 simultaneously and 
// log both names when both requests complete.
Promise.all([
    fetchUserPromise(1),
    fetchUserPromise(2)
])
.then(users => {
    console.log("User 1:", users[0].name);
    console.log("User 2:", users[1].name);
})
.catch(error => {
    console.error("Error:", error);
});


// 50. Create a reusable async function apiFetch(url) that fetches data, checks response.ok, 
// throws a descriptive Error if not ok, and returns the parsed JSON.
async function apiFetch(url) {
    try {
        const response = await fetch(url);

        if (!response.ok) {
            throw new Error(
                `HTTP Error ${response.status}: ${response.statusText}`
            );
        }

        const data = await response.json();
        return data;
    }
    catch (error) {
        throw error;
    }
}


// 51. Use apiFetch to load posts from /posts and render them as notification cards in a 
// new <section id='notifications'> on the page.
const notificationList = document.querySelector("#notification-list");

function renderNotifications(posts) {
    notificationList.innerHTML = "";

    posts.forEach(post => {
        const card = document.createElement("article");
        card.className = "notification-card";

        card.innerHTML = `
            <h3>${post.title}</h3>
            <p>${post.body}</p>
        `;

        notificationList.appendChild(card);
    });
}

apiFetch("https://jsonplaceholder.typicode.com/posts")
    .then(posts => {
        renderNotifications(posts.slice(0, 5));
    })
    .catch(error => {
        console.error(error);
    });


// 52. Add a loading spinner (a simple animated CSS div or a text indicator) that appears 
// while the fetch is in-progress and disappears when data loads.
const loadingSpinner = document.querySelector("#loading-spinner");
loadingSpinner.classList.remove("hidden");

apiFetch("https://jsonplaceholder.typicode.com/posts")
    .then(posts => {
        renderNotifications(posts.slice(0,5));
    })
    .catch(error => {
        console.error(error);
    })
    .finally(() => {
        loadingSpinner.classList.add("hidden");
    });


// 53. Simulate a 404 error by calling apiFetch with a bad URL (e.g., /nonexistent). 
// Display a user-friendly error message in the UI — never just log to console.
const errorMessage = document.querySelector("#error-message");
loadingSpinner.classList.remove("hidden");

apiFetch("https://jsonplaceholder.typicode.com/nonexistent")
    .then(posts => {
        renderNotifications(posts);
    })
    .catch(error => {
        errorMessage.style.display = "block";
        errorMessage.textContent = "Unable to load notifications. Please try again later.";
    })
    .finally(() => {
        loadingSpinner.classList.add("hidden");
    });


// 54. Add a Retry button that appears when an error occurs. On click, 
// it re-calls the fetch function and re-renders the section.
const retryButton = document.querySelector("#retry-btn");

async function loadNotifications(url) {
    loadingSpinner.classList.remove("hidden");
    errorMessage.style.display = "none";
    retryButton.classList.add("hidden");
    notificationList.innerHTML = "";

    try {
        const posts = await apiFetch(url);
        renderNotifications(posts.slice(0, 5));
    }
    catch (error) {
        errorMessage.style.display = "block";
        errorMessage.textContent = "Unable to load notifications. Please try again.";
        retryButton.classList.remove("hidden");
    }
    finally {
        loadingSpinner.classList.add("hidden");
    }
}
loadNotifications("https://jsonplaceholder.typicode.com/nonexistent");

retryButton.addEventListener("click", () => {
    loadNotifications("https://jsonplaceholder.typicode.com/posts");
});


// 56. Rewrite the apiFetch function using axios.get(url). Note that Axios: (a) automatically parses JSON, 
// (b) throws on non-2xx responses by default — no need to check response.ok manually.
async function apiFetchAxios(url) {
    try {
        const response = await axios.get(url);
        return response.data;
    }
    catch (error) {
        throw error;
    }
}


// 57. Use axios.get with a params object: axios.get('/posts', { params: { userId: 1 } }) 
// to fetch posts belonging to user 1.
async function fetchUserPosts() {
    try {
        const response = await axios.get(
            "https://jsonplaceholder.typicode.com/posts",
            {
                params: {
                    userId: 1
                }
            }
        );

        console.log(response.data);
        renderNotifications(response.data);
    }
    catch (error) {
        console.error(error);
    }
}
fetchUserPosts();


// 58. Add a request interceptor using axios.interceptors.request.use() that logs 
// 'API call started: <url>' before every request.
axios.interceptors.request.use(
    function (config) {
        console.log(`API call started: ${config.url}`);
        return config;
    },
    function (error) {
        return Promise.reject(error);
    }
);