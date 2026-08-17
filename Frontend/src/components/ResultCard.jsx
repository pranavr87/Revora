function ResultCard({ diagnosis }) {

    if (!diagnosis) {
        return (
            <div style={{ marginTop: "40px", textAlign: "center" }}>
                <h2>Diagnosis Result</h2>
                <p>Diagnosis result will come here.</p>
            </div>
        );
    }

    return (

        <div
            style={{
                width: "70%",
                margin: "40px auto",
                padding: "25px",
                borderRadius: "12px",
                backgroundColor: "#1f2937",
                color: "white",
                boxShadow: "0 0 15px rgba(0,0,0,0.4)"
            }}
        >

            <h2 style={{ textAlign: "center" }}>
                🚗 Diagnosis Result
            </h2>

            <hr />

            <p><b>🔧 Fault:</b> {diagnosis.fault}</p>

            <p><b>⚠ Root Cause:</b> {diagnosis.root_cause}</p>

            <p><b>🛠 Solution:</b> {diagnosis.solution}</p>

            <p><b>💰 Estimated Cost:</b> {diagnosis.estimated_cost}</p>

            <p><b>⏱ Repair Time:</b> {diagnosis.repair_time}</p>

            <p>
                <b>🚨 Severity:</b>{" "}
                <span
                    style={{
                        color:
                            diagnosis.severity === "High"
                                ? "red"
                                : diagnosis.severity === "Medium"
                                ? "orange"
                                : "lightgreen"
                    }}
                >
                    {diagnosis.severity}
                </span>
            </p>

        </div>

    );
}

export default ResultCard;