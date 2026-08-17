import { useState } from "react";
import api from "../services/api";
import "../styles/DiagnosisResult.css";

import {
    FaExclamationTriangle,
    FaTools,
    FaWrench,
    FaRupeeSign,
    FaClock,
    FaFilePdf
} from "react-icons/fa";

function DiagnosisResult({

    diagnosis,

    brand,

    model,

    symptom

}) {

    const [downloading, setDownloading] = useState(false);

    const downloadPDF = async () => {

        if (!diagnosis) return;

        try {

            setDownloading(true);

            const response = await api.post(

                "/vehicles/report",

                {

                    brand,

                    model,

                    symptom

                },

                {

                    responseType: "blob"

                }

            );

            const blob = new Blob(

                [response.data],

                {

                    type: "application/pdf"

                }

            );

            const url = window.URL.createObjectURL(blob);

            const link = document.createElement("a");

            link.href = url;

            link.download = "REVORA_Report.pdf";

            document.body.appendChild(link);

            link.click();

            document.body.removeChild(link);

            window.URL.revokeObjectURL(url);

        }

        catch (error) {

            console.error(error);

            alert("Failed to download PDF.");

        }

        finally {

            setDownloading(false);

        }

    };

    if (!diagnosis) {

        return (

            <div className="result-card">

                <h2>Diagnosis Result</h2>

                <div className="empty-result">

                    <div>

                        <h3
                            style={{
                                color: "white",
                                marginBottom: "15px"
                            }}
                        >
                            No Diagnosis Yet
                        </h3>

                        <p>

                            Select your vehicle details and click

                            <strong> Analyze Vehicle </strong>

                            to generate the diagnosis report.

                        </p>

                    </div>

                </div>

            </div>

        );

    }

    return (

        <div className="result-card">

            <h2>Diagnosis Result</h2>

            <div className="result-box">

                <div className="result-title">

                    <FaExclamationTriangle />

                    <span>

                        Detected Fault

                    </span>

                </div>

                <div className="result-value">

                    {diagnosis.fault}

                </div>

            </div>

            <div className="result-box">

                <div className="result-title">

                    <FaTools />

                    <span>

                        Root Cause

                    </span>

                </div>

                <div className="result-value">

                    {diagnosis.root_cause}

                </div>

            </div>

            <div className="result-box">

                <div className="result-title">

                    <FaWrench />

                    <span>

                        Recommended Solution

                    </span>

                </div>

                <div className="result-value">

                    {diagnosis.solution}

                </div>

            </div>

            <div className="cost-time">

                <div className="small-card">

                    <h4>

                        <FaRupeeSign />

                        {" "}Estimated Cost

                    </h4>

                    <p>

                        {diagnosis.estimated_cost}

                    </p>

                </div>

                <div className="small-card">

                    <h4>

                        <FaClock />

                        {" "}Repair Time

                    </h4>

                    <p>

                        {diagnosis.repair_time}

                    </p>

                </div>

            </div>

            <button

                className="pdf-btn"

                onClick={downloadPDF}

                disabled={downloading}

            >

                <FaFilePdf />

                {" "}

                {

                    downloading

                        ? "Generating PDF..."

                        : "Download PDF Report"

                }

            </button>

        </div>

    );

}

export default DiagnosisResult;