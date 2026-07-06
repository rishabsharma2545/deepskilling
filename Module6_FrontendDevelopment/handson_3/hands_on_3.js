// 29. Create a data.js file and export a const array of 5 course objects, 
// each with id, name, code, credits, and grade properties.

// 30. In app.js, import the array using ES6 import. Use destructuring to extract 
// name and credits from each course in a loop.

// 31. Use Array.map() to create a new array of strings formatted as 
// 'CS101 — Data Structures (4 credits)'. Log the result.

// 32. Use Array.filter() to get only courses with credits >= 4. Log the count.

// 33. Use Array.reduce() to calculate the total credits enrolled. Log the result.

// 34. Rewrite an existing for loop in your code as an arrow function. 
// Use a template literal for string interpolation.

// 35. In index.html, ensure the course grid <div class='course-grid'> exists 
// but is empty (remove hardcoded course articles).

// 36. In app.js, use document.querySelector('.course-grid') to select the grid container.

// 37. Loop through your course data array. For each course, create a <article> element using document.createElement(), 
// set its className, and build its inner HTML using a template literal with course name, code, and credits.

// 38. Append each created article to the course grid using appendChild().

// 39. Add a <p id='total-credits'> below the grid. After rendering, 
// update its textContent to display the total credits dynamically.

// 40. Add a text <input id='search-courses' placeholder='Search courses...'> above the course grid.

// 41. Add an event listener on the input's 'input' event. On each keystroke, 
// filter the course array by name (case-insensitive) and re-render only the matching cards.

// 42. Add a 'Sort by Credits' <button>. On click, sort the courses array by credits descending and re-render the grid.

// 43. Add a click event to each course card: when clicked, display an alert 
// (or update a <div id='selected course'>) showing the course name and grade.

// 44. Use event delegation: attach a single click listener to the course-grid container 
// and detect which card was clicked using event.target.closest('.course-card').