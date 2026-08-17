import { useNavigate } from "react-router-dom";
import { FaArrowRight, FaCheckCircle } from "react-icons/fa";

import heroImage from "../assets/hero-illustration.png";

import "../styles/Hero.css";

function Hero() {

    const navigate = useNavigate();

    const scrollToFeatures = () => {

        const section = document.getElementById("why");

        if (section) {

            section.scrollIntoView({
                behavior: "smooth"
            });

        }

    };

    return (

        <section className="hero">

            <div className="hero-container">

                {/* LEFT */}

                <div className="hero-left fade-left">

                    <span className="hero-tag">

                        Vehicle Diagnostics Platform

                    </span>

                    <h1>

                        REVORA

                    </h1>

                    <h2>

                        From Symptoms to Solutions.

                    </h2>

                    <p>

                        Identify vehicle faults, understand root causes,
                        estimate repair costs, and receive reliable
                        maintenance guidance through a single intelligent
                        platform.

                    </p>

                    <div className="hero-buttons">

                        <button
                            className="primary-btn"
                            onClick={() => navigate("/diagnosis")}
                        >

                            Start Diagnosis

                            <FaArrowRight />

                        </button>

                        <button
                            className="secondary-btn"
                            onClick={scrollToFeatures}
                        >

                            Learn More

                        </button>

                    </div>

                    <div className="hero-features">

                        <span>

                            <FaCheckCircle />

                            Fast Diagnosis

                        </span>

                        <span>

                            <FaCheckCircle />

                            PDF Report

                        </span>

                        <span>

                            <FaCheckCircle />

                            Reliable Results

                        </span>

                    </div>

                </div>

                {/* RIGHT */}

                <div className="hero-right fade-right">

                    <img
                        src={heroImage}
                        alt="Vehicle Diagnostics"
                    />

                </div>

            </div>

        </section>

    );

}

export default Hero;