from io import BytesIO
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
)


BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR / "static"

LOGO_PATH = STATIC_DIR / "revora_logo.png"


def generate_pdf(data):

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=18 * mm,
        bottomMargin=18 * mm,
        title="REVORA Vehicle Diagnosis Report",
        author="REVORA",
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "RevoraTitle",
        parent=styles["Title"],
        fontSize=26,
        leading=30,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#0B1B3A"),
        spaceAfter=5,
    )

    subtitle_style = ParagraphStyle(
        "RevoraSubtitle",
        parent=styles["Normal"],
        fontSize=11,
        leading=15,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#5B6472"),
        spaceAfter=15,
    )

    heading_style = ParagraphStyle(
        "SectionHeading",
        parent=styles["Heading2"],
        fontSize=14,
        leading=18,
        textColor=colors.HexColor("#1677FF"),
        spaceBefore=4,
        spaceAfter=7,
    )

    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontSize=10,
        leading=15,
        textColor=colors.HexColor("#202733"),
    )

    small_style = ParagraphStyle(
        "Small",
        parent=styles["Normal"],
        fontSize=8.5,
        leading=12,
        textColor=colors.HexColor("#6B7280"),
    )

    story = []

    # -----------------------------
    # LOGO
    # -----------------------------

    if LOGO_PATH.exists():

        logo = Image(
            str(LOGO_PATH),
            width=42 * mm,
            height=15 * mm,
        )

        logo.hAlign = "CENTER"

        story.append(logo)
        story.append(Spacer(1, 4 * mm))

    # -----------------------------
    # TITLE
    # -----------------------------

    story.append(
        Paragraph(
            "REVORA",
            title_style
        )
    )

    story.append(
        Paragraph(
            "Vehicle Fault Diagnosis Report",
            subtitle_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Generated On:</b> "
            f"{data.get('generated_on', '-')}",
            small_style
        )
    )

    story.append(Spacer(1, 7 * mm))

    # -----------------------------
    # VEHICLE DETAILS
    # -----------------------------

    story.append(
        Paragraph(
            "Vehicle Details",
            heading_style
        )
    )

    vehicle_data = [
        [
            Paragraph("<b>Brand</b>", body_style),
            Paragraph(
                str(data.get("brand", "-")),
                body_style
            ),
        ],
        [
            Paragraph("<b>Model</b>", body_style),
            Paragraph(
                str(data.get("model", "-")),
                body_style
            ),
        ],
        [
            Paragraph("<b>Symptom</b>", body_style),
            Paragraph(
                str(data.get("symptom", "-")),
                body_style
            ),
        ],
    ]

    vehicle_table = Table(
        vehicle_data,
        colWidths=[
            45 * mm,
            125 * mm
        ],
    )

    vehicle_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#EAF2FF"),
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.8,
                colors.HexColor("#B8C7DD"),
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#D7DFEA"),
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "TOP",
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                9,
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                9,
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                10,
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                10,
            ),
        ])
    )

    story.append(vehicle_table)

    story.append(Spacer(1, 9 * mm))

    # -----------------------------
    # DIAGNOSIS
    # -----------------------------

    story.append(
        Paragraph(
            "Diagnosis",
            heading_style
        )
    )

    diagnosis_data = [
        [
            Paragraph(
                "<b>Detected Fault</b>",
                body_style
            ),
            Paragraph(
                str(data.get("fault", "-")),
                body_style
            ),
        ],
        [
            Paragraph(
                "<b>Root Cause</b>",
                body_style
            ),
            Paragraph(
                str(data.get("root_cause", "-")),
                body_style
            ),
        ],
        [
            Paragraph(
                "<b>Recommended Solution</b>",
                body_style
            ),
            Paragraph(
                str(data.get("solution", "-")),
                body_style
            ),
        ],
        [
            Paragraph(
                "<b>Severity</b>",
                body_style
            ),
            Paragraph(
                str(data.get("severity", "-")),
                body_style
            ),
        ],
    ]

    diagnosis_table = Table(
        diagnosis_data,
        colWidths=[
            55 * mm,
            115 * mm
        ],
    )

    diagnosis_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (0, -1),
                colors.HexColor("#F3F7FC"),
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.8,
                colors.HexColor("#B8C7DD"),
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#D7DFEA"),
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "TOP",
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                10,
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                10,
            ),
            (
                "LEFTPADDING",
                (0, 0),
                (-1, -1),
                10,
            ),
            (
                "RIGHTPADDING",
                (0, 0),
                (-1, -1),
                10,
            ),
        ])
    )

    story.append(diagnosis_table)

    story.append(Spacer(1, 9 * mm))

    # -----------------------------
    # COST & REPAIR TIME
    # -----------------------------

    cost_data = [
        [
            Paragraph(
                "<b>Estimated Repair Cost</b>",
                body_style
            ),
            Paragraph(
                "<b>Estimated Repair Time</b>",
                body_style
            ),
        ],
        [
            Paragraph(
                str(data.get("estimated_cost", "-")),
                body_style
            ),
            Paragraph(
                str(data.get("repair_time", "-")),
                body_style
            ),
        ],
    ]

    cost_table = Table(
        cost_data,
        colWidths=[
            85 * mm,
            85 * mm
        ],
    )

    cost_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.HexColor("#EAF2FF"),
            ),
            (
                "BACKGROUND",
                (0, 1),
                (-1, 1),
                colors.HexColor("#F8FAFC"),
            ),
            (
                "BOX",
                (0, 0),
                (-1, -1),
                0.8,
                colors.HexColor("#B8C7DD"),
            ),
            (
                "INNERGRID",
                (0, 0),
                (-1, -1),
                0.5,
                colors.HexColor("#D7DFEA"),
            ),
            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER",
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE",
            ),
            (
                "TOPPADDING",
                (0, 0),
                (-1, -1),
                10,
            ),
            (
                "BOTTOMPADDING",
                (0, 0),
                (-1, -1),
                10,
            ),
        ])
    )

    story.append(cost_table)

    story.append(Spacer(1, 14 * mm))

    # -----------------------------
    # DISCLAIMER
    # -----------------------------

    story.append(
        Paragraph(
            "<b>Note:</b> This report provides an automated "
            "diagnostic suggestion based on the selected vehicle "
            "and symptom. Actual vehicle faults should be "
            "confirmed by a qualified automotive professional.",
            small_style
        )
    )

    story.append(Spacer(1, 7 * mm))

    story.append(
        Paragraph(
            "REVORA • From Symptoms to Solutions.",
            subtitle_style
        )
    )

    # -----------------------------
    # BUILD PDF
    # -----------------------------

    document.build(story)

    return buffer.getvalue()