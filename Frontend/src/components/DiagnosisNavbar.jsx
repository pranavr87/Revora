import { NavLink } from "react-router-dom";
import logo from "../assets/logo.png";

import "../styles/Navbar.css";

function DiagnosisNavbar() {

    return (

        <nav className="navbar">

            <div className="navbar-container">

                <div className="navbar-logo">

                    <img
                        src={logo}
                        alt="REVORA"
                    />

                    <h2>REVORA</h2>

                </div>

                <div className="navbar-links">

                    <NavLink
                        to="/"
                    >
                        Home
                    </NavLink>

                    <span className="active-link">

                        Diagnosis

                    </span>

                </div>

            </div>

        </nav>

    );

}

export default DiagnosisNavbar;