import { NavLink } from "react-router-dom";
import logo from "../assets/logo.png";

import "../styles/Navbar.css";

function LandingNavbar() {

    const scrollToSection = (id) => {

        const section = document.getElementById(id);

        if (section) {

            section.scrollIntoView({
                behavior: "smooth"
            });

        }

    };

    return (

        <nav className="navbar">

            <div className="navbar-container">

                <div className="navbar-logo">

                    <img src={logo} alt="REVORA"/>

                    <h2>REVORA</h2>

                </div>

                <div className="navbar-links">

                    <button
                        onClick={() => scrollToSection("why")}
                    >
                        Features
                    </button>

                    <button
                        onClick={() => scrollToSection("works")}
                    >
                        How It Works
                    </button>

                </div>

                <NavLink
                    to="/diagnosis"
                    className="navbar-btn"
                >
                    Diagnosis
                </NavLink>

            </div>

        </nav>

    );

}

export default LandingNavbar;