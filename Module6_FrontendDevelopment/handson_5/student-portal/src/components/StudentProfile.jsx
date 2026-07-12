// 74. Create a separate StudentProfile.jsx component with its own local state (name, email, semester). 
// Add a form with inputs bound to state via onChange handlers.

import { useState } from "react";

function StudentProfile() {
    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [semester, setSemester] = useState("");

    return (
        <section className="student-profile">

            <h2>Student Profile</h2>

            <form>
                <div>
                    <label>Name:</label>
                    <input
                        type="text"
                        value={name}
                        onChange={(event) =>
                            setName(event.target.value)
                        }
                    />
                </div>

                <div>
                    <label>Email:</label>
                    <input
                        type="email"
                        value={email}
                        onChange={(event) =>
                            setEmail(event.target.value)
                        }
                    />
                </div>

                <div>
                    <label>Semester:</label>
                    <input
                        type="number"
                        value={semester}
                        onChange={(event) =>
                            setSemester(event.target.value)
                        }
                    />
                </div>
            </form>

            <hr />
            <h3>Profile Preview</h3>
            <p><strong>Name:</strong> {name}</p>
            <p><strong>Email:</strong> {email}</p>
            <p><strong>Semester:</strong> {semester}</p>

        </section>

    );

}

export default StudentProfile;