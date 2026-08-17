from app.database.connection import get_connection


def get_all_brands():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT brand
        FROM indian_vehicles
        WHERE brand NOT IN (
            'Nissan',
            'SML Isuzu',
            'Force Motors',
            'Renault'
        )
        ORDER BY brand
    """)

    brands = cursor.fetchall()

    conn.close()

    return brands


def get_models_by_brand(brand):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT model
        FROM indian_vehicles
        WHERE brand = ?
        AND model IS NOT NULL
        AND TRIM(model) != ''
        ORDER BY model
    """, (brand,))

    models = cursor.fetchall()

    conn.close()

    return models


def get_all_symptoms():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT standard_symptom
        FROM fault_knowledge
        ORDER BY standard_symptom
    """)

    symptoms = cursor.fetchall()

    conn.close()

    return symptoms


def diagnose_fault(symptom):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            possible_fault,
            root_cause,
            recommended_solution,
            estimated_cost_min_inr,
            estimated_cost_max_inr,
            repair_time_min_hours,
            repair_time_max_hours,
            severity
        FROM fault_knowledge
        WHERE LOWER(standard_symptom) = LOWER(?)
        LIMIT 1
    """, (symptom,))

    result = cursor.fetchone()

    conn.close()

    return result


def get_standard_symptom_from_alias(alias):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT standard_symptom
        FROM symptom_aliases
        WHERE LOWER(TRIM(alias)) = LOWER(TRIM(?))
        LIMIT 1
    """, (alias,))

    result = cursor.fetchone()

    conn.close()

    return result


def search_symptoms(keyword):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT DISTINCT standard_symptom
        FROM symptom_aliases
        WHERE LOWER(standard_symptom) LIKE LOWER(?)
        ORDER BY standard_symptom
        LIMIT 20
    """, (f"%{keyword}%",))

    rows = cursor.fetchall()

    conn.close()

    return [
        row["standard_symptom"]
        for row in rows
    ]