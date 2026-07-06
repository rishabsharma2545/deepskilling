// 14. Revisit the <header> in your existing index.html and styles.css from Hands-On 1.

// 15. Apply display: flex on the header. Use align-items: center and justify-content: space-between.

// 16. Style the <nav> as a flex container with gap between items. Ensure links are vertically centred.

// 17. Create a hero section using Flexbox: stack the heading, paragraph, 
// and button vertically with align-items: center and a column flex-direction.

// 18. Add a student stats bar below the hero with three stat items (e.g., Courses Enrolled: 3, GPA: 3.8, Semester: 6). 
// Lay them out using Flexbox with equal spacing.

// 19. Wrap all three course <article> elements in a <div class='course-grid'>.

// 20. Apply display: grid on .course-grid with grid-template-columns: repeat(3, 1fr) and a gap.

// 21. Give each .course-card a minimum height and make it stretch to fill its grid cell using align-self: stretch.

// 22. Add two more course cards (total 5) and observe how the grid automatically places them.

// 23. Use grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)) — 
// observe how the grid adapts as you resize the browser window.

// 24. Rewrite your existing CSS to be mobile-first: start with a single-column layout as the default 
// (no media queries), then use min-width media queries to enhance larger screens.

// 25. Add a media query at min-width: 768px: change the course grid to 2 columns 
// and show the full navbar (replace a hamburger placeholder text with the actual nav links).

// 26. Add a media query at min-width: 1024px: change the course grid to 3 columns 
// and increase hero section padding.

// 27. Use viewport units: set the hero section min-height: 40vh and the site title font-size 
// to clamp(1.5rem, 3vw, 2.5rem) for fluid typography.

// 28. Open DevTools and use the device toolbar to test the layout at 375px (mobile), 768px (tablet), 
// and 1280px (desktop). Fix any overflow or layout breaks.