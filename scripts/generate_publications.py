from pathlib import Path
from datetime import date
import re

from pybtex.database import parse_file
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    KeepTogether,
)


ROOT = Path(__file__).resolve().parent.parent
BIB_FILE = ROOT / "_bibliography" / "papers.bib"
OUTPUT_FILE = ROOT / "assets" / "pdf" / "publications.pdf"

MY_FAMILY_NAME = "Papageorgiou"


def clean_latex(text):
    if not text:
        return ""

    replacements = {
        r"\&": "&",
        r"\%": "%",
        r"\_": "_",
        r"\textendash": "–",
        "---": "—",
        "--": "–",
        "{": "",
        "}": "",
    }

    for old, new in replacements.items():
        text = text.replace(old, new)

    return text


def person_name(person):
    first = " ".join(person.first_names + person.middle_names)
    last = " ".join(person.prelast_names + person.last_names)

    name = f"{first} {last}".strip()
    name = clean_latex(name)

    if MY_FAMILY_NAME.lower() in name.lower():
        return f"<b>{name}</b>"

    return name


def authors(entry):
    people = entry.persons.get("author", [])
    names = [person_name(person) for person in people]

    if not names:
        return ""

    if len(names) == 1:
        return names[0]

    if len(names) == 2:
        return f"{names[0]} and {names[1]}"

    return ", ".join(names[:-1]) + f", and {names[-1]}"


def year_of(entry):
    try:
        return int(entry.fields.get("year", "0"))
    except ValueError:
        return 0


def is_ifac(entry):
    journal = clean_latex(entry.fields.get("journal", ""))
    return "IFAC-PapersOnLine" in journal


def category(entry):
    entry_type = entry.type.lower()

    if entry_type == "article" and not is_ifac(entry):
        return "Journal Articles"

    if entry_type in ("inproceedings", "conference") or (
        entry_type == "article" and is_ifac(entry)
    ):
        return "Conference Papers"

    if entry_type in ("phdthesis", "mastersthesis", "thesis"):
        return "Theses"

    if entry_type in ("book", "inbook", "incollection"):
        return "Books & Book Chapters"

    return None


def citation(entry):
    fields = entry.fields

    author_text = authors(entry)
    title = clean_latex(fields.get("title", ""))
    year = clean_latex(fields.get("year", ""))

    pieces = []

    if author_text:
        pieces.append(author_text)

    if title:
        pieces.append(f'“{title}”')

    if entry.type.lower() == "article":
        venue = clean_latex(fields.get("journal", ""))
    else:
        venue = clean_latex(
            fields.get("booktitle", "")
            or fields.get("school", "")
            or fields.get("publisher", "")
        )

    if venue:
        pieces.append(f"<i>{venue}</i>")

    volume = clean_latex(fields.get("volume", ""))
    number = clean_latex(fields.get("number", ""))
    pages = clean_latex(fields.get("pages", ""))

    if volume:
        volume_text = f"vol. {volume}"
        if number:
            volume_text += f", no. {number}"
        pieces.append(volume_text)

    if pages:
        pieces.append(f"pp. {pages}")

    if year:
        pieces.append(year)

    text = ", ".join(pieces) + "."

    doi = clean_latex(fields.get("doi", ""))
    if doi:
        doi_url = f"https://doi.org/{doi}"
        text += (
            f' DOI: <link href="{doi_url}" color="#555555">{doi}</link>'
        )

    # Basic protection against accidental duplicated spaces
    return re.sub(r"\s+", " ", text)


def build_pdf():
    bibliography = parse_file(str(BIB_FILE), bib_format="bibtex")

    grouped = {
        "Journal Articles": [],
        "Conference Papers": [],
        "Books & Book Chapters": [],
        "Theses": [],
    }

    for key, entry in bibliography.entries.items():
        section = category(entry)
        if section:
            grouped[section].append((key, entry))

    for section in grouped:
        grouped[section].sort(
            key=lambda item: (year_of(item[1]), item[0]),
            reverse=True,
        )

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(OUTPUT_FILE),
        pagesize=A4,
        rightMargin=2.0 * cm,
        leftMargin=2.0 * cm,
        topMargin=1.8 * cm,
        bottomMargin=1.8 * cm,
        title="List of Publications",
        author="Dimitrios Papageorgiou",
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "PublicationTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=18,
        leading=22,
        spaceAfter=4,
    )

    subtitle_style = ParagraphStyle(
        "PublicationSubtitle",
        parent=styles["Normal"],
        alignment=TA_CENTER,
        fontSize=10,
        textColor=colors.HexColor("#666666"),
        spaceAfter=20,
    )

    heading_style = ParagraphStyle(
        "PublicationHeading",
        parent=styles["Heading2"],
        fontSize=13,
        leading=16,
        spaceBefore=12,
        spaceAfter=8,
    )

    entry_style = ParagraphStyle(
        "PublicationEntry",
        parent=styles["BodyText"],
        fontSize=9.5,
        leading=13,
        spaceAfter=7,
    )

    story = [
        Paragraph("Dimitrios Papageorgiou", title_style),
        Paragraph("List of Publications", styles["Heading2"]),
        Paragraph(
            f"Generated from the publication database · {date.today():%B %Y}",
            subtitle_style,
        ),
    ]

    for section_name, entries in grouped.items():
        if not entries:
            continue

        story.append(Paragraph(section_name, heading_style))

        for number, (_, entry) in enumerate(entries, start=1):
            item = Paragraph(
                f"[{number}]&nbsp;&nbsp;{citation(entry)}",
                entry_style,
            )
            story.append(KeepTogether([item]))

        story.append(Spacer(1, 4))

    doc.build(story)

    print(f"Generated {OUTPUT_FILE}")


if __name__ == "__main__":
    build_pdf()