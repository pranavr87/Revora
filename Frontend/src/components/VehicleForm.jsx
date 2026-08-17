import { useEffect, useState } from "react";
import api from "../services/api";
import "../styles/VehicleForm.css";

function VehicleForm({

    setDiagnosis,

    selectedBrand,
    setSelectedBrand,

    selectedModel,
    setSelectedModel,

    selectedSymptom,
    setSelectedSymptom

}) {

    const [brands, setBrands] = useState([]);

    const [models, setModels] = useState([]);

    const [symptoms, setSymptoms] = useState([]);

    const [loading, setLoading] = useState(false);

    useEffect(() => {

        api.get("/vehicles/brands")

            .then((response) => {

                setBrands(response.data.brands);

            })

            .catch((error) => {

                console.log(error);

            });

        api.get("/vehicles/symptoms")

            .then((response) => {

                setSymptoms(response.data.symptoms);

            })

            .catch((error) => {

                console.log(error);

            });

    }, []);

    const loadModels = (brand) => {

        setSelectedBrand(brand);

        setSelectedModel("");

        if (brand === "") {

            setModels([]);

            return;

        }

        api.get(`/vehicles/models/${brand}`)

            .then((response) => {

                setModels(response.data.models);

            })

            .catch((error) => {

                console.log(error);

            });

    };

    const diagnoseVehicle = () => {

        if (

            selectedBrand === "" ||

            selectedModel === "" ||

            selectedSymptom === ""

        ) {

            alert("Please select Brand, Model and Symptom.");

            return;

        }

        setLoading(true);

        api.post("/vehicles/diagnose", {

            brand: selectedBrand,

            model: selectedModel,

            symptom: selectedSymptom

        })

        .then((response) => {

            setTimeout(() => {

                setDiagnosis(response.data);

                setLoading(false);

            }, 2000);

        })

        .catch((error) => {

            console.log(error);

            setLoading(false);

        });

    };
        return (

        <div className="vehicle-form">

            <div className="form-header">

                <h2>

                    Vehicle Details

                </h2>

                <p>

                    Fill the details below to analyze your vehicle.

                </p>

            </div>

            <div className="ai-status">

                <span className="status-dot"></span>

                AI Diagnosis System Ready

            </div>

            <div className="form-group">

                <label>

                    Vehicle Brand

                </label>

                <select

                    className="form-control"

                    value={selectedBrand}

                    onChange={(e) => loadModels(e.target.value)}

                >

                    <option value="">

                        Select Brand

                    </option>

                    {

                        brands.map((brand, index) => (

                            <option

                                key={index}

                                value={brand}

                            >

                                {brand}

                            </option>

                        ))

                    }

                </select>

            </div>

            <div className="form-group">

                <label>

                    Vehicle Model

                </label>

                <select

                    className="form-control"

                    value={selectedModel}

                    disabled={!selectedBrand}

                    onChange={(e) => setSelectedModel(e.target.value)}

                >

                    <option value="">

                        Select Model

                    </option>

                    {

                        models

                            .filter(model => model)

                            .map((model, index) => (

                                <option

                                    key={index}

                                    value={model}

                                >

                                    {model}

                                </option>

                            ))

                    }

                </select>

            </div>

            <div className="form-group">

                <label>

                    Vehicle Symptom

                </label>

                <select

                    className="form-control"

                    value={selectedSymptom}

                    disabled={!selectedModel}

                    onChange={(e) => setSelectedSymptom(e.target.value)}

                >

                    <option value="">

                        Select Symptom

                    </option>

                    {

                        symptoms.map((symptom, index) => (

                            <option

                                key={index}

                                value={symptom.value}

                            >

                                {symptom.label}

                            </option>

                        ))

                    }

                </select>

            </div>

            {

                !loading &&

                <button

                    className="diagnose-btn"

                    onClick={diagnoseVehicle}

                >

                    Analyze Vehicle

                </button>

            }

            {

                loading &&

                <div className="loading-box">

                    <div className="loader"></div>

                    <h3>

                        REVORA AI

                    </h3>

                    <p>

                        Analyzing your vehicle...

                    </p>

                    <div className="loading-steps">

                        <span>🔍 Connecting to Diagnosis Engine...</span>

                        <span>⚙ Matching Fault Database...</span>

                        <span>🚗 Identifying Root Cause...</span>

                        <span>📄 Preparing Diagnosis Report...</span>

                    </div>

                </div>

            }

        </div>

    );

}

export default VehicleForm;