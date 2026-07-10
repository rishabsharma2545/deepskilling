// 45. Write a function fetchUser(id) that calls fetch('https://jsonplaceholder.typicode.com/users/' + id) 
// and returns a Promise. Chain .then() to parse the JSON and log the user's name.

// 46. Rewrite the same function using async/await and try/catch.

// 47. Write a function fetchAllCourses() that simulates a 1-second network delay using 
// new Promise(resolve => setTimeout(resolve, 1000)) and then returns your local course array.

// 48. Call fetchAllCourses() and render the course cards only after the promise resolves. 
// Show a 'Loading courses...' message while waiting.

// 49. Demonstrate Promise.all(): fetch user ID 1 and user ID 2 simultaneously and 
// log both names when both requests complete.

// 50. Create a reusable async function apiFetch(url) that fetches data, checks response.ok, 
// throws a descriptive Error if not ok, and returns the parsed JSON.

// 51. Use apiFetch to load posts from /posts and render them as notification cards in a 
// new <section id='notifications'> on the page.

// 52. Add a loading spinner (a simple animated CSS div or a text indicator) that appears 
// while the fetch is in-progress and disappears when data loads.

// 53. Simulate a 404 error by calling apiFetch with a bad URL (e.g., /nonexistent). 
// Display a user-friendly error message in the UI — never just log to console.

// 54. Add a Retry button that appears when an error occurs. On click, 
// it re-calls the fetch function and re-renders the section.

// 55. Add Axios via CDN in your HTML: 
// <script src='https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js'></script>.

// 56. Rewrite the apiFetch function using axios.get(url). Note that Axios: (a) automatically parses JSON, 
// (b) throws on non-2xx responses by default — no need to check response.ok manually.

// 57. Use axios.get with a params object: axios.get('/posts', { params: { userId: 1 } }) 
// to fetch posts belonging to user 1.

// 58. Add a request interceptor using axios.interceptors.request.use() that logs 
// 'API call started: <url>' before every request.

// 59. Compare: write a side-by-side comment in your code listing three differences between fetch and axios.
/*
>>> Fetch API vs Axios

1. JSON Parsing
~~~~~~~~~~~~~~~~
Fetch:
    const response = await fetch(url);
    const data = await response.json();

Axios:
    const response = await axios.get(url);
    const data = response.data;

Axios automatically parses JSON.


2. Error Handling
~~~~~~~~~~~~~~~~~~
Fetch:
    Does NOT throw errors for HTTP status codes like
    404 or 500.
    We must manually check:

        if (!response.ok) {
            throw new Error("Request Failed");
        }

Axios:
    Automatically throws an error for non-2xx responses.
    No need to check response.ok.


3. Query Parameters
~~~~~~~~~~~~~~~~~~~~
Fetch:
    Query parameters must be written manually.

        fetch("/posts?userId=1");

Axios:
    Supports a params object.

        axios.get("/posts", {
            params: {
                userId: 1
            }
        });

Axios automatically builds the query string.
*/

