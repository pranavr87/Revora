import re


def normalize_text(text: str) -> str:
    """
    Normalize user input before searching the database.
    """

    text = text.lower().strip()

    replacements = {
        "kr": "kar",
        "nhi": "nahi",
        "_": " ",
        "?": "",
        ".": "",
        ",": "",
        "hai": "",
        "please": "",
        "pls": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"\s+", " ", text).strip()

    return text