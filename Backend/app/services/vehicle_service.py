from app.database.queries import (
    get_all_brands,
    get_models_by_brand,
    get_all_symptoms,
    diagnose_fault,
    get_standard_symptom_from_alias,
    search_symptoms,
)

from app.utils.text_utils import normalize_text
from app.utils.pdf_generator import generate_pdf


def fetch_brands():
    rows = get_all_brands()
    return [row["brand"] for row in rows]


def fetch_models(brand):
    rows = get_models_by_brand(brand)
    return [row["model"] for row in rows]


def fetch_symptoms():
    rows = get_all_symptoms()

    symptoms = []

    for row in rows:

        value = row["standard_symptom"]

        label = value.replace("_", " ").title()

        label = label.replace("Abs", "ABS")
        label = label.replace("Ac", "AC")
        label = label.replace("Dpf", "DPF")
        label = label.replace("Egr", "EGR")
        label = label.replace("Scr", "SCR")
        label = label.replace("Tpms", "TPMS")

        symptoms.append({
            "value": value,
            "label": label
        })

    return symptoms


def fetch_diagnosis(symptom):

    original_input = symptom

    symptom = normalize_text(symptom)

    alias = get_standard_symptom_from_alias(symptom)

    if alias:
        symptom = alias["standard_symptom"]
    else:
        symptom = symptom.replace(" ", "_")

    row = diagnose_fault(symptom)

    if row is None:
        return {
            "success": False,
            "message": "No diagnosis found.",
            "searched": symptom,
            "suggestion": "Try another symptom."
        }

    return {
        "success": True,
        "user_input": original_input,
        "matched_symptom": symptom,
        "fault": row["possible_fault"],
        "root_cause": row["root_cause"],
        "solution": row["recommended_solution"],
        "estimated_cost": f"₹{row['estimated_cost_min_inr']} - ₹{row['estimated_cost_max_inr']}",
        "repair_time": f"{row['repair_time_min_hours']} - {row['repair_time_max_hours']} Hours",
        "severity": row["severity"]
    }


def fetch_multiple_diagnosis(symptoms):

    results = []

    symptom_list = symptoms.split(" and ")

    for symptom in symptom_list:

        results.append(
            fetch_diagnosis(symptom.strip())
        )

    return results


def fetch_search_results(keyword):
    return search_symptoms(keyword)


from datetime import datetime

def fetch_pdf_report(brand, model, symptom):

    diagnosis = fetch_diagnosis(symptom)

    if not diagnosis["success"]:
        return None

    diagnosis["brand"] = brand

    diagnosis["model"] = model

    diagnosis["user_input"] = symptom.replace("_", " ").title()

    diagnosis["generated_on"] = datetime.now().strftime(
        "%d %b %Y %I:%M %p"
    )

    return generate_pdf(diagnosis)