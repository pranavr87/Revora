import { useState } from "react";

import DiagnosisNavbar from "../components/DiagnosisNavbar";
import VehicleForm from "../components/VehicleForm";
import DiagnosisResult from "../components/DiagnosisResult";

import "../styles/Diagnosis.css";

function Diagnosis() {

    const [diagnosis, setDiagnosis] = useState(null);

    const [selectedBrand, setSelectedBrand] = useState("");

    const [selectedModel, setSelectedModel] = useState("");

    const [selectedSymptom, setSelectedSymptom] = useState("");

    return (

        <>

            <DiagnosisNavbar />

            <div className="diagnosis-page">

                <div className="diagnosis-left">

                    <VehicleForm

                        setDiagnosis={setDiagnosis}

                        selectedBrand={selectedBrand}
                        setSelectedBrand={setSelectedBrand}

                        selectedModel={selectedModel}
                        setSelectedModel={setSelectedModel}

                        selectedSymptom={selectedSymptom}
                        setSelectedSymptom={setSelectedSymptom}

                    />

                </div>

                <div className="diagnosis-right">

                    <DiagnosisResult

                        diagnosis={diagnosis}

                        brand={selectedBrand}

                        model={selectedModel}

                        symptom={selectedSymptom}

                    />

                </div>

            </div>

        </>

    );

}

export default Diagnosis;