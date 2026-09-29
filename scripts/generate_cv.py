from pathlib import Path
from datetime import date
import html
import re
import sys

import yaml
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
    Image,
)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(
    TTFont(
        "Arial",
        "/System/Library/Fonts/Supplemental/Arial.ttf"
    )
)

pdfmetrics.registerFont(
    TTFont(
        "Arial-Bold",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
    )
)

pdfmetrics.registerFont(
    TTFont(
        "Arial-Italic",
        "/System/Library/Fonts/Supplemental/Arial Italic.ttf"
    )
)

pdfmetrics.registerFont(
    TTFont(
        "Arial-BoldItalic",
        "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf"
    )
)

pdfmetrics.registerFontFamily(
    "Arial",
    normal="Arial",
    bold="Arial-Bold",
    italic="Arial-Italic",
    boldItalic="Arial-BoldItalic",
)

# ---------------------------------------------------------
# Paths
# ---------------------------------------------------------

ROOT = Path(__file__).resolve().parent.parent

CV_FILE = ROOT / "_data" / "cv.yml"
PHD_FILE = ROOT / "_data" / "phd_students.yml"
POSTDOC_FILE = ROOT / "_data" / "postdocs.yml"
STUDENTS_FILE = ROOT / "_data" / "students.yml"
FUNDERS_FILE = ROOT / "_data" / "funders.yml"
METRICS_FILE = ROOT / "_data" / "metrics.yml"
PROFILE_IMAGE = ROOT / "assets" / "img" / "prof_pic.jpg"

PROJECTS_DIR = ROOT / "_research_projects"

CV_MODES = {
    "full": {
        "output": ROOT / "assets" / "pdf" / "cv.pdf",
        "exclude_sections": [],
    },
    "2page": {
        "output": ROOT / "private" / "cv-2page.pdf",
        "exclude_sections": [
            "Invited Talks & Visibility",
        ],
    },
    "1page": {
        "output": ROOT / "private" / "cv-1page.pdf",
        "exclude_sections": [
            "Invited Talks & Visibility",
            "Awards & Distinctions",
            "Research Interests",
            "Teaching",
            "Academic Service",
        ],
    },
}


# ---------------------------------------------------------
# General helpers
# ---------------------------------------------------------

def load_yaml(path, default=None):
    if default is None:
        default = []

    if not path.exists():
        return default

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    return data if data is not None else default


def esc(value):
    """Escape text for ReportLab Paragraph markup."""
    if value is None:
        return ""

    return html.escape(str(value))


def clean_text(value):
    if value is None:
        return ""

    value = str(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def year_sort_value(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return 0


# ---------------------------------------------------------
# Read research-project front matter
# ---------------------------------------------------------

def read_front_matter(path):
    text = path.read_text(encoding="utf-8")

    # Handle normal Jekyll front matter.
    match = re.match(
        r"^\s*---\s*\n(.*?)\n---\s*(?:\n|$)",
        text,
        flags=re.DOTALL,
    )

    if not match:
        return None

    data = yaml.safe_load(match.group(1))
    return data if isinstance(data, dict) else None


def load_projects():
    projects = []

    if not PROJECTS_DIR.exists():
        return projects

    for path in PROJECTS_DIR.glob("*.md"):
        data = read_front_matter(path)

        if not data:
            continue

        data["_source"] = path.name
        projects.append(data)

    projects.sort(
        key=lambda p: (
            year_sort_value(p.get("start_year")),
            p.get("importance", 0),
        ),
        reverse=True,
    )

    return projects


# ---------------------------------------------------------
# Funder handling
# ---------------------------------------------------------

def funder_name(funder_id, funders):
    if not funder_id:
        return ""

    if isinstance(funders, dict):
        funder = funders.get(funder_id)

        if isinstance(funder, dict):
            return clean_text(funder.get("name", funder_id))

    return clean_text(funder_id)


def project_funders(project, funders):
    value = project.get("funders")

    if not value:
        return ""

    # YAML may contain either one string or a list.
    if isinstance(value, str):
        ids = [value]
    else:
        ids = value

    names = [funder_name(x, funders) for x in ids]
    return ", ".join(x for x in names if x)


# ---------------------------------------------------------
# Supervision calculations
# Mirrors _includes/cv/supervision.html
# ---------------------------------------------------------

def supervision_summary():
    phds = load_yaml(PHD_FILE, [])
    postdocs = load_yaml(POSTDOC_FILE, [])
    students = load_yaml(STUDENTS_FILE, [])

    current_phds = [x for x in phds if x.get("status") == "current"]
    former_phds = [x for x in phds if x.get("status") == "former"]

    current_postdocs = [
        x for x in postdocs if x.get("status") == "current"
    ]
    former_postdocs = [
        x for x in postdocs if x.get("status") == "former"
    ]

    former_students = [
        x for x in students if x.get("status") == "former"
    ]

    former_msc = [
        x for x in former_students if x.get("type") == "MSc"
    ]
    former_bsc = [
        x for x in former_students if x.get("type") == "BSc"
    ]

    unique_msc_titles = {
        x.get("title")
        for x in former_msc
        if x.get("title")
    }

    unique_bsc_titles = {
        x.get("title")
        for x in former_bsc
        if x.get("title")
    }

    return [
        (
            "<b>PhD supervision:</b> "
            f"{len(phds)} candidates · "
            f"{len(current_phds)} current · "
            f"{len(former_phds)} completed"
        ),
        (
            "<b>Postdoctoral supervision:</b> "
            f"{len(postdocs)} researchers · "
            f"{len(current_postdocs)} current · "
            f"{len(former_postdocs)} former"
        ),
        (
            "<b>Student supervision:</b> "
            f"{len(former_students)} completed projects · "
            f"{len(unique_msc_titles)} MSc theses · "
            f"{len(unique_bsc_titles)} BSc projects"
        ),
    ]


# ---------------------------------------------------------
# PDF styles
# ---------------------------------------------------------

styles = getSampleStyleSheet()

NAME_STYLE = ParagraphStyle(
    "CVName",
    parent=styles["Title"],
    fontName="Arial-Bold",
    fontSize=17,
    leading=19,
    alignment=TA_CENTER,
    spaceAfter=2,
)

SUBTITLE_STYLE = ParagraphStyle(
    "CVSubtitle",
    parent=styles["Normal"],
    fontName="Arial",
    fontSize=9,
    leading=11,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#444444"),
    spaceAfter=2,
)

META_STYLE = ParagraphStyle(
    "CVMeta",
    parent=SUBTITLE_STYLE,
    fontSize=8,
    leading=10,
    spaceAfter=8,
)

ACCENT = colors.HexColor("#3F6F8F")

SECTION_STYLE = ParagraphStyle(
    "CVSection",
    parent=styles["Heading2"],
    fontName="Arial-Bold",
    fontSize=10.5,
    leading=12,
    spaceBefore=8,
    spaceAfter=4,
    textColor=ACCENT,
    leftIndent=0,
    rightIndent=0,
    firstLineIndent=0,
)

DATE_STYLE = ParagraphStyle(
    "CVDate",
    parent=styles["Normal"],
    fontName="Arial",
    fontSize=7.8,
    leading=9.5,
    textColor=colors.HexColor("#666666"),
)

ENTRY_STYLE = ParagraphStyle(
    "CVEntry",
    parent=styles["Normal"],
    fontName="Arial",
    fontSize=8.5,
    leading=10.7,
    spaceAfter=0,
)

ENTRY_TITLE_STYLE = ParagraphStyle(
    "CVEntryTitle",
    parent=ENTRY_STYLE,
    fontName="Arial-Bold",
)

SMALL_STYLE = ParagraphStyle(
    "CVSmall",
    parent=ENTRY_STYLE,
    fontSize=8.1,
    leading=10.2,
)


# ---------------------------------------------------------
# PDF building helpers
# ---------------------------------------------------------

def add_section_heading(story, title):
    heading_style = ParagraphStyle(
        "SectionHeadingAligned",
        parent=SECTION_STYLE,
        leftIndent=0,
        rightIndent=0,
        firstLineIndent=0,
        spaceBefore=8,
        spaceAfter=2,
    )

    story.append(
        Paragraph(
            esc(title).upper(),
            heading_style,
        )
    )

    rule = Table(
        [[""]],
        colWidths=[16.6 * cm],
        rowHeights=[1],
        hAlign="LEFT",
    )

    rule.setStyle(
        TableStyle([
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ("LINEBELOW", (0, 0), (-1, -1), 0.5, ACCENT),
        ])
    )

    story.append(rule)
    story.append(Spacer(1, 3))


def add_timed_entry(
    story,
    year,
    title="",
    institution="",
    description=None,
    title_markup=None,
):
    if description is None:
        description = []

    right = []

    if title_markup:
        right.append(title_markup)
    elif title:
        right.append(f"<b>{esc(clean_text(title))}</b>")

    if institution:
        right.append(esc(clean_text(institution)))

    for item in description:
        if item:
            right.append(esc(clean_text(item)))

    right_text = "<br/>".join(right)

    table = Table(
        [[
            Paragraph(esc(clean_text(year)), DATE_STYLE),
            Paragraph(right_text, ENTRY_STYLE),
        ]],
        colWidths=[2.25 * cm, 14.35 * cm],
        hAlign="LEFT",
    )

    table.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),

            # Small inset for the date column
            ("LEFTPADDING", (0, 0), (0, -1), 0),

            # Keep the main content aligned with the section headings
            ("LEFTPADDING", (1, 0), (1, -1), 0),

            ("RIGHTPADDING", (0, 0), (0, -1), 7),
            ("RIGHTPADDING", (1, 0), (1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 1.2),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 2.0),
        ])
    )

    story.append(table)


def add_list_section(story, contents):
    for item in contents:
        story.append(
            Paragraph(
                "• " + esc(clean_text(item)),
                ENTRY_STYLE,
            )
        )


def add_tags(story, contents):
    text = " · ".join(clean_text(x) for x in contents)
    story.append(Paragraph(esc(text), ENTRY_STYLE))


def add_map(story, contents):
    rows = []

    for item in contents:
        rows.append([
            Paragraph(
                f"<b>{esc(clean_text(item.get('name', '')))}</b>",
                ENTRY_STYLE,
            ),
            Paragraph(
                esc(clean_text(item.get("value", ""))),
                ENTRY_STYLE,
            ),
        ])

    table = Table(
        rows,
        colWidths=[3.0 * cm, 13.6 * cm],
        hAlign="LEFT",
    )

    table.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
            ("TOPPADDING", (0, 0), (-1, -1), 1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ])
    )

    story.append(table)


# ---------------------------------------------------------
# Research projects
# ---------------------------------------------------------

def add_projects(story, funders, mode="full"):
    projects = load_projects()

    for project in projects:
        start = project.get("start_year", "")
        end = project.get("end_year")

        if start and end:
            period = f"{start}–{end}"
        elif start:
            period = f"{start}–Present"
        else:
            period = ""

        title = clean_text(project.get("title", ""))
        full_title = clean_text(project.get("full_title", ""))
        role = clean_text(project.get("role", ""))

        details = []

        # Don't repeat full_title if it is identical to title.
        if full_title and full_title.lower() != title.lower():
            details.append(full_title)

        funder = project_funders(project, funders)
        programme = clean_text(project.get("programme", ""))

        funding_line = funder

        if programme:
            if funding_line:
                funding_line += f" · {programme}"
            else:
                funding_line = programme

        if funding_line:
            details.append(funding_line)

        if role:
            project_heading = f"<b>{esc(title)}</b> · {esc(role)}"
        else:
            project_heading = f"<b>{esc(title)}</b>"
        
        if mode == "1page":
            budget = project.get("budget")
            currency = clean_text(project.get("currency", ""))

            if budget:
                budget_millions = float(budget) / 1_000_000
                budget_text = f"{budget_millions:.2f}M {esc(currency)}"

                project_heading = (
                    f"<b>{esc(title)}</b>"
                    f" · {budget_text}"
                )

                if role:
                    project_heading += f" · {esc(role)}"

            add_timed_entry(
                story,
                period,
                description=None,
                title_markup=project_heading,
            )
            continue

        add_timed_entry(
            story,
            period,
            description=details,
            title_markup=project_heading,
        )
# ---------------------------------------------------------
# Main CV renderer
# ---------------------------------------------------------

def build_pdf(mode="full"):
    config = CV_MODES[mode]
    output_file = config["output"]
    cv_data = load_yaml(CV_FILE, [])
    funders = load_yaml(FUNDERS_FILE, {})

    output_file.parent.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(output_file),
        pagesize=A4,
        leftMargin=1.55 * cm,
        rightMargin=1.55 * cm,
        topMargin=1.35 * cm,
        bottomMargin=1.35 * cm,
        title="Curriculum Vitae — Dimitrios Papageorgiou",
        author="Dimitrios Papageorgiou",
    )

    story = []

    # -----------------------------------------------------
    # Header
    # -----------------------------------------------------

    metrics = load_yaml(METRICS_FILE, {})

    scholar = metrics.get("google_scholar", {})
    scopus = metrics.get("scopus", {})

    header_text = []

    header_text.append(
        Paragraph(
            "Dimitrios Papageorgiou",
            ParagraphStyle(
                "HeaderName",
                parent=NAME_STYLE,
                alignment=0,
                fontSize=18,
                leading=20,
                spaceAfter=4,
            ),
        )
    )

    header_text.append(
        Paragraph(
            "<b>Associate Professor of Nonlinear and Fault-Tolerant Control</b>",
            ParagraphStyle(
                "HeaderPosition",
                parent=ENTRY_STYLE,
                fontSize=9.5,
                leading=12,
                spaceAfter=4,
            ),
        )
    )

    header_text.append(
        Paragraph(
            "Technical University of Denmark (DTU)<br/>"
            "Department of Electrical and Photonics Engineering<br/>"
            "Control, Robotics and Embodied AI (CREA)<br/>"
            "Building 326, Room 124 · 2800 Kgs. Lyngby, Denmark<br/>"
            "dimpa@dtu.dk",
            ParagraphStyle(
                "HeaderContact",
                parent=ENTRY_STYLE,
                fontSize=9,
                leading=11.5,
                spaceAfter=0,
            ),
        )
    )

    header_text.append(Spacer(1, 5))

    header_text.append(
        Paragraph(
            "<b>ORCID:</b> 0000-0002-4900-4083<br/>"
            f"<b>H-index:</b> {scholar.get('h_index', '—')} Google Scholar"
            f" · {scopus.get('h_index', '—')} Scopus<br/>"
            f"<b>Citations:</b> {scholar.get('citations', '—')} Google Scholar"
            f" · {scopus.get('citations', '—')} Scopus",
            ParagraphStyle(
                "HeaderMetrics",
                parent=SMALL_STYLE,
                fontSize=8.5,
                leading=11,
            ),
        )
    )

    if PROFILE_IMAGE.exists():
        photo = Image(str(PROFILE_IMAGE))
        photo.drawHeight = 4.5 * cm
        photo.drawWidth = photo.imageWidth * photo.drawHeight / photo.imageHeight

        header = Table(
            [[photo, header_text]],
            colWidths=[4.0 * cm, 12.6 * cm],
            hAlign="LEFT",
        )
    else:
        header = Table(
            [["", header_text]],
            colWidths=[0.1 * cm, 16.5 * cm],
            hAlign="LEFT",
        )

    header.setStyle(
        TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("TOPPADDING", (0, 0), (-1, -1), 0),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ])
    )

    story.append(header)

    story.append(Spacer(1, 4))

    header_rule = Table(
        [[""]],
        colWidths=[16.6 * cm],
        rowHeights=[1],
        hAlign="LEFT",
    )

    header_rule.setStyle(
        TableStyle([
            ("LEFTPADDING", (0, 0), (-1, -1), 0),
            ("RIGHTPADDING", (0, 0), (-1, -1), 0),
            ("LINEBELOW", (0, 0), (-1, -1), 0.8, ACCENT),
        ])
    )

    story.append(header_rule)
    story.append(Spacer(1, 3))
    # -----------------------------------------------------
    # Sections from cv.yml
    # -----------------------------------------------------

    for entry in cv_data:
        title = entry.get("title", "")
        entry_type = entry.get("type", "")
        contents = entry.get("contents", [])

        # Full publication list belongs in publications.pdf. Skip sections that should not appear in the PDF CV.
        if entry_type == "publications":
            continue
        
        if title == "Contact Information":
            continue

        if title in config.get("exclude_sections", []):
            continue
        
        add_section_heading(story, title)

        if entry_type == "time_table":
            for item in contents:
                # Some entries (e.g. awards) use year + items.
                if "items" in item:
                    items = item.get("items", [])

                    for index, text in enumerate(items):
                        add_timed_entry(
                            story,
                            item.get("year", "") if index == 0 else "",
                            description=[text],
                        )

                else:
                    description = item.get("description", [])

                    if isinstance(description, str):
                        description = [description]

                    add_timed_entry(
                        story,
                        item.get("year", ""),
                        title=item.get("title", ""),
                        institution=item.get("institution", ""),
                        description=description,
                    )

        elif entry_type == "tags":
            add_tags(story, contents)

        elif entry_type == "list":
            add_list_section(story, contents)

        elif entry_type == "map":
            add_map(story, contents)

        elif entry_type == "research_projects":
            add_projects(story, funders, mode=mode)

        elif entry_type == "supervision":
            for line in supervision_summary():
                story.append(
                    Paragraph(
                        line,
                        ENTRY_STYLE,
                    )
                )

        # Any unsupported/custom type is deliberately skipped
        # rather than guessing how it should be rendered.

        story.append(Spacer(1, 1.5))

    doc.build(story)

    print(f"Generated {output_file}")


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "full"

    if mode not in CV_MODES:
        valid_modes = ", ".join(CV_MODES.keys())
        raise SystemExit(
            f"Unknown CV mode: {mode}\n"
            f"Available modes: {valid_modes}"
        )

    build_pdf(mode)