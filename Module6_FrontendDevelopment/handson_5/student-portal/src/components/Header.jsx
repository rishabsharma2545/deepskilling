// 62. Create Header.jsx — a functional component that renders the site title and a nav bar with links (Home, Courses, Profile).

function Header(props) {
    return (
        <header>
            <h1>{props.siteName}</h1>

            <nav>
                <ul>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Courses</a></li>
                    <li><a href="#">Profile</a></li>
                </ul>
            </nav>

            <p>
                Enrolled Courses: {props.enrolledCount}
            </p>
            
        </header>
    );
}

export default Header;