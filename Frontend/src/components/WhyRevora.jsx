import "../styles/WhyRevora.css";
import {
    FaCar,
    FaSearch,
    FaTools,
    FaBolt
} from "react-icons/fa";

function WhyRevora() {

    const features = [

        {
            icon: <FaCar />,
            title: "Vehicle Specific",
            description:
                "Diagnose faults based on the selected vehicle brand and model."
        },

        {
            icon: <FaSearch />,
            title: "Accurate Diagnosis",
            description:
                "Identify the most probable fault using structured vehicle data."
        },

        {
            icon: <FaTools />,
            title: "Complete Solution",
            description:
                "Get root cause analysis, repair guidance and estimated repair cost."
        },

        {
            icon: <FaBolt />,
            title: "Instant Results",
            description:
                "Generate diagnosis reports within seconds."
        }

    ];

    return (

        <section className="why-section">

            <div className="why-header">

                <h2>
    Why Choose REVORA
</h2>

<p>
    Designed to deliver accurate vehicle diagnostics,
    reliable repair guidance, and faster decision-making.
</p>
            </div>

            <div className="why-grid">

                {

                    features.map((item, index) => (

                        <div
                            className="why-card"
                            key={index}
                        >

                            <div className="why-icon">

                                {item.icon}

                            </div>

                            <h3>

                                {item.title}

                            </h3>

                            <p>

                                {item.description}

                            </p>

                        </div>

                    ))

                }

            </div>

        </section>

    );

}

export default WhyRevora;