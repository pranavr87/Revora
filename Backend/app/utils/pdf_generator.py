import os
import tempfile
from pathlib import Path

from playwright.sync_api import sync_playwright
from jinja2 import Environment, FileSystemLoader


BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = BASE_DIR / "templates"

STATIC_DIR = BASE_DIR / "static"


env = Environment(

    loader=FileSystemLoader(TEMPLATE_DIR),

    auto_reload=True,

    cache_size=0

)


template = env.get_template("report.html")


def generate_pdf(data):

    html = template.render(

        logo_path=f"file:///{STATIC_DIR/'revora_logo.png'}",

        css_path=f"file:///{STATIC_DIR/'report.css'}",

        generated_on=data.get("generated_on"),

        brand=data.get("brand"),

        model=data.get("model"),

        symptom=data.get("user_input"),

        fault=data.get("fault"),

        root_cause=data.get("root_cause"),

        solution=data.get("solution"),

        estimated_cost=data.get("estimated_cost"),

        repair_time=data.get("repair_time"),

        severity=data.get("severity")

    )

    temp = tempfile.NamedTemporaryFile(

        suffix=".html",

        delete=False,

        mode="w",

        encoding="utf-8"

    )

    temp.write(html)
    print(html)

    temp.close()

    html_file = Path(temp.name)

    with sync_playwright() as p:

        browser = p.chromium.launch(

            headless=True

        )

        page = browser.new_page()

        page.set_viewport_size({
            "width": 1280,
            "height": 1810
        })

        page.goto(

            html_file.as_uri(),

            wait_until="networkidle"

        )
        page.wait_for_timeout(500)

        page.pdf(

            path=str(

                html_file.with_suffix(".pdf")

            ),

            format="A4",

            print_background=True,

            margin={

                "top": "20px",

                "bottom": "20px",

                "left": "20px",

                "right": "20px"

            }

        )

        browser.close()

    pdf_path = html_file.with_suffix(

        ".pdf"

    )

    with open(

        pdf_path,

        "rb"

    ) as f:

        pdf_bytes = f.read()

    if html_file.exists():

        html_file.unlink()

    if pdf_path.exists():

        pdf_path.unlink()

    return pdf_bytes