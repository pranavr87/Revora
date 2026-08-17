import { useNavigate } from "react-router-dom";
import logo from "../assets/logo.png";

import "../styles/Hero.css";

function Hero() {

    const navigate = useNavigate();

    return (

        <section className="hero">

            <div className="hero-overlay"></div>

            <div className="hero-content">

                <img
                    src={logo}
                    alt="REVORA Logo"
                    className="hero-logo"
                />

                <h1 className="hero-title">
                    REVORA
                </h1>

                <h2 className="hero-subtitle">
                    From Symptoms to Solutions.
                </h2>

                <p className="hero-description">
                    Diagnose vehicle faults with confidence using accurate
                    fault detection, root cause analysis, repair cost estimation,
                    and maintenance recommendations — all in one place.
                </p>

                <button
                    className="hero-btn"
                    onClick={() => navigate("/diagnosis")}
                >
                    Start Diagnosis
                </button>

            </div>

            <div className="scroll-indicator">
                ↓
            </div>

        </section>

    );

}

export default Hero;