function StatsCard() {

    return (

        <div
            style={{
                marginTop: "50px",
                textAlign: "center"
            }}
        >

            <h2>✨ Why Choose Our System?</h2>

            <div
                style={{
                    display: "flex",
                    justifyContent: "center",
                    flexWrap: "wrap",
                    gap: "20px",
                    marginTop: "30px"
                }}
            >

                <div style={cardStyle}>
                    <h3>🚗 Vehicle Specific </h3>
                    <p>
                        Diagnose faults based on the selected
                        vehicle brand and model.
                    </p>
                </div>

                <div style={cardStyle}>
                    <h3>🔍 Smart Diagnosis</h3>
                    <p>
                        Matches vehicle symptoms with the
                        knowledge base to detect faults.
                    </p>
                </div>

                <div style={cardStyle}>
                    <h3>🛠 Complete Solution</h3>
                    <p>
                        Provides root cause, repair solution,
                        estimated cost and repair time.
                    </p>
                </div>

                <div style={cardStyle}>
                    <h3>⚡ Instant Results</h3>
                    <p>
                        Get diagnosis instantly without
                        manually searching service manuals.
                    </p>
                </div>

            </div>

        </div>

    );

}

const cardStyle = {

    width: "250px",

    padding: "25px",

    backgroundColor: "#1f2937",

    color: "white",

    borderRadius: "15px",

    boxShadow: "0 0 15px rgba(0,0,0,0.4)",

    transition: "0.3s"

};

export default StatsCard;