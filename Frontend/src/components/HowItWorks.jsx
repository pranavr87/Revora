import "../styles/HowItWorks.css";
import {
  FaCarSide,
  FaSearch,
  FaMicrochip,
  FaFileAlt,
} from "react-icons/fa";

function HowItWorks() {
  const steps = [
    {
      icon: <FaCarSide />,
      title: "Choose Vehicle",
      text: "Select your vehicle brand and model.",
    },
    {
      icon: <FaSearch />,
      title: "Select Symptoms",
      text: "Choose the symptoms your vehicle is experiencing.",
    },
    {
      icon: <FaMicrochip />,
      title: "AI Diagnosis",
      text: "REVORA analyzes thousands of fault records instantly.",
    },
    {
      icon: <FaFileAlt />,
      title: "View Report",
      text: "Receive fault analysis, repair cost and maintenance guidance.",
    },
  ];

  return (
    <section className="works-section" id="works">
      <div className="works-header">
        <h2>How It Works</h2>
        <p>Diagnose your vehicle in four simple steps.</p>
      </div>

      <div className="timeline">
        {steps.map((step, index) => (
          <div className="timeline-item" key={index}>
            <div className="timeline-icon">
              {step.icon}
            </div>

            <div className="timeline-content">
              <h3>{step.title}</h3>
              <p>{step.text}</p>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default HowItWorks;