
import os
import re
from datetime import datetime

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
from pypdf import PdfReader
from docx import Document


# --------------------------------------------------
# TESSERACT CONFIGURATION
# --------------------------------------------------

pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


# --------------------------------------------------
# EXTRACT TEXT FROM IMAGE
# --------------------------------------------------

def extract_image_text(image):
    """Extract text from an image using Tesseract OCR."""

    image = image.convert("RGB")

    # Increase image size for better OCR
    image = image.resize(
        (image.width * 2, image.height * 2)
    )

    # Convert to grayscale
    image = image.convert("L")

    # Improve contrast
    image = ImageEnhance.Contrast(image).enhance(2)

    # Sharpen image
    image = image.filter(ImageFilter.SHARPEN)

    # Extract text
    text = pytesseract.image_to_string(
        image,
        config="--psm 6"
    )

    return text.strip()


# --------------------------------------------------
# EXTRACT TEXT FROM DOCX
# --------------------------------------------------

def extract_docx_text(file_path):
    """Read text from Word document paragraphs and tables."""

    document = Document(file_path)

    extracted_text = []

    # Read paragraphs
    for paragraph in document.paragraphs:

        text = paragraph.text.strip()

        if text:
            extracted_text.append(text)

    # Read tables
    for table in document.tables:

        for row in table.rows:

            row_text = []

            for cell in row.cells:

                cell_text = cell.text.strip()

                if cell_text:
                    row_text.append(cell_text)

            if row_text:
                extracted_text.append(
                    " ".join(row_text)
                )

    return "\n".join(extracted_text).strip()


# --------------------------------------------------
# EXTRACT TEXT FROM IMAGE, PDF, OR DOCX
# --------------------------------------------------

def extract_text(file_path):

    extension = os.path.splitext(
        file_path
    )[1].lower()

    # PDF
    if extension == ".pdf":

        extracted_text = []

        reader = PdfReader(file_path)

        try:
            import fitz
            pdf_document = fitz.open(file_path)

        except ImportError:
            pdf_document = None

        for page_number, page in enumerate(reader.pages):

            page_text = page.extract_text() or ""

            if page_text.strip():

                extracted_text.append(page_text)

            elif pdf_document is not None:

                # OCR for scanned PDF pages
                try:

                    pdf_page = pdf_document[page_number]

                    pix = pdf_page.get_pixmap(
                        matrix=fitz.Matrix(2, 2)
                    )

                    image = Image.frombytes(
                        "RGB",
                        (pix.width, pix.height),
                        pix.samples
                    )

                    extracted_text.append(
                        extract_image_text(image)
                    )

                except Exception as error:

                    print(
                        "PDF OCR error:",
                        error
                    )

        if pdf_document is not None:
            pdf_document.close()

        return "\n".join(
            extracted_text
        ).strip()

    # IMAGE
    elif extension in (
        ".jpg",
        ".jpeg",
        ".png",
        ".bmp"
    ):

        with Image.open(file_path) as image:

            return extract_image_text(image)

    # WORD DOCUMENT
    elif extension == ".docx":

        return extract_docx_text(file_path)

    # UNSUPPORTED FILE
    else:

        raise ValueError(
            "Unsupported file format. "
            "Upload JPG, JPEG, PNG, BMP, PDF, or DOCX."
        )


# --------------------------------------------------
# NORMALIZE TEXT
# --------------------------------------------------

def normalize_text(text):

    if not text:
        return ""

    text = text.replace("\r", "\n")

    text = re.sub(
        r"[ \t]+",
        " ",
        text
    )

    return text.strip()


# --------------------------------------------------
# FIND EVENT DATE
# --------------------------------------------------

def find_date(text):

    if not text:
        return None

    text = normalize_text(text)

    # Find labeled date first
    patterns = [

        r"(?im)^\s*date\s*[:\-]?\s*"
        r"(\d{1,2}[./-]\d{1,2}[./-]\d{4})",

        r"\b(\d{1,2}[./-]\d{1,2}[./-]\d{4})\b",

        r"(?im)^\s*date\s*[:\-]?\s*"
        r"(\d{1,2}\s+[A-Za-z]+\s+\d{4}|"
        r"[A-Za-z]+\s+\d{1,2},?\s+\d{4})",

        r"\b(\d{1,2}\s+[A-Za-z]+\s+\d{4}|"
        r"[A-Za-z]+\s+\d{1,2},?\s+\d{4})\b",
    ]

    candidate = None

    for pattern in patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            candidate = match.group(1)

            break

    if not candidate:
        return None

    # Indian numeric date format: DD/MM/YYYY
    date_formats = [

        "%d/%m/%Y",
        "%d-%m-%Y",
        "%d.%m.%Y",

        "%d %B %Y",
        "%d %b %Y",

        "%B %d %Y",
        "%B %d, %Y",

        "%b %d %Y",
        "%b %d, %Y",
    ]

    for date_format in date_formats:

        try:

            return datetime.strptime(
                candidate,
                date_format
            ).date()

        except ValueError:

            continue

    return None


# --------------------------------------------------
# NORMALIZE TIME TEXT
# --------------------------------------------------

def normalize_time_text(text):

    if not text:
        return ""

    text = text.upper()

    # Convert 8.00 PM or 8,00 PM to 8:00 PM
    text = re.sub(
        r"(\d{1,2})[.,](\d{2})\s*([AP])\.?\s*M\.?",
        r"\1:\2 \3M",
        text
    )

    # Normalize A.M. and P.M.
    text = re.sub(
        r"\bA\.?\s*M\.?\b",
        "AM",
        text
    )

    text = re.sub(
        r"\bP\.?\s*M\.?\b",
        "PM",
        text
    )

    return text


# --------------------------------------------------
# FIND EVENT TIME
# --------------------------------------------------

def find_time(text):

    if not text:
        return None

    text = normalize_time_text(text)

    # Ignore next-day wording
    text = re.sub(
        r"\bNEXT\s+DAY\b|\bTHE FOLLOWING DAY\b",
        "",
        text,
        flags=re.IGNORECASE
    )

    # Find 12-hour time
    match = re.search(
        r"\b(\d{1,2})(?::(\d{2}))?\s*(AM|PM)\b",
        text,
        flags=re.IGNORECASE
    )

    if match:

        hour = int(match.group(1))

        minute = int(
            match.group(2) or 0
        )

        meridiem = match.group(3).upper()

        if not (
            1 <= hour <= 12
            and 0 <= minute <= 59
        ):
            return None

        # Convert to 24-hour format
        if meridiem == "AM":

            hour = 0 if hour == 12 else hour

        else:

            hour = 12 if hour == 12 else hour + 12

        return f"{hour:02d}:{minute:02d}"

    # Find 24-hour time
    match = re.search(
        r"\b([01]?\d|2[0-3]):([0-5]\d)\b",
        text
    )

    if match:

        return (
            f"{int(match.group(1)):02d}:"
            f"{int(match.group(2)):02d}"
        )

    return None


# --------------------------------------------------
# FIND EVENT TITLE
# --------------------------------------------------

def find_event_title(text):

    if not text:
        return None

    text = normalize_text(text)

    # FIRST: Find title using explicit labels
    # Example: Event Name: Diwali Party

    title_patterns = [

        r"(?im)^\s*event\s*name\s*[:\-]\s*(.+?)\s*$",

        r"(?im)^\s*event\s*title\s*[:\-]\s*(.+?)\s*$",

        r"(?im)^\s*title\s*[:\-]\s*(.+?)\s*$",
    ]

    for pattern in title_patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            title = match.group(1).strip()

            title = re.sub(
                r"\s+",
                " ",
                title
            )

            if title:

                return title[:250]

    # SECOND: Check known event keywords

    event_keywords = [

        "workshop",
        "conference",
        "birthday",
        "wedding",
        "engagement",
        "annual day",
        "farewell",
        "reunion",
        "graduation",
        "celebration",
        "seminar",
    ]

    for event_name in event_keywords:

        if re.search(
            rf"\b{re.escape(event_name)}\b",
            text,
            re.IGNORECASE
        ):

            return event_name.title()

    # THIRD: Use the first suitable non-detail line

    ignored_labels = (

        "venue",
        "location",
        "address",
        "date",
        "time",
        "contact",
        "phone",
        "email",
    )

    for line in text.splitlines():

        line = line.strip()

        if (
            line
            and not line.lower().startswith(ignored_labels)
        ):

            return line[:250]

    return None


# --------------------------------------------------
# FIND EVENT VENUE
# --------------------------------------------------

def find_venue(text):

    if not text:
        return None

    lines = [

        line.strip()

        for line in normalize_text(text).splitlines()

        if line.strip()
    ]

    venue_labels = (

        "venue",
        "location",
        "address",
        "place",
        "held at",
        "organized at",
        "organised at",
    )

    # Find venue using labels

    for line in lines:

        for label in venue_labels:

            pattern = (

                rf"(?i)^\s*{re.escape(label)}"
                rf"\s*[:\-]\s*(.*?)\s*$"
            )

            match = re.search(
                pattern,
                line
            )

            if match:

                venue = match.group(1).strip()

                if venue:

                    return clean_venue(venue)

    # Fallback for common venue names

    venue_patterns = [

        r"\b[A-Za-z][A-Za-z ]+Seminar Hall\b",

        r"\b[A-Za-z][A-Za-z ]+Auditorium\b",

        r"\b[A-Za-z][A-Za-z ]+Conference Hall\b",

        r"\b[A-Za-z][A-Za-z ]+College Hall\b",
    ]

    for line in lines:

        for pattern in venue_patterns:

            match = re.search(
                pattern,
                line,
                flags=re.IGNORECASE
            )

            if match:

                return clean_venue(
                    match.group(0)
                )

    return None


# --------------------------------------------------
# CLEAN VENUE
# --------------------------------------------------

def clean_venue(venue):

    if not venue:
        return None

    venue = venue.strip()

    # Remove dates
    venue = re.sub(
        r"\b\d{1,2}[./-]\d{1,2}[./-]\d{4}\b",
        "",
        venue
    )

    venue = re.sub(
        r"\b\d{1,2}\s+[A-Za-z]+\s+\d{4}\b|"
        r"\b[A-Za-z]+\s+\d{1,2},?\s+\d{4}\b",
        "",
        venue,
        flags=re.IGNORECASE
    )

    # Remove time
    venue = re.sub(
        r"\b\d{1,2}(?::\d{2})?\s*(?:AM|PM)\b",
        "",
        venue,
        flags=re.IGNORECASE
    )

    # Remove extra symbols
    venue = re.sub(
        r"^[\s:=,\-–—]+|[\s:=,\-–—]+$",
        "",
        venue
    )

    venue = re.sub(
        r"\s+",
        " ",
        venue
    ).strip()

    if len(venue) < 3:

        return None

    return venue[:250]


# --------------------------------------------------
# FIND EVENT DESCRIPTION
# --------------------------------------------------

def find_description(text):

    if not text:
        return None

    lines = [

        line.strip()

        for line in text.splitlines()

        if line.strip()
    ]

    description_lines = []

    ignored_labels = (

        "event name:",
        "event title:",
        "title:",
        "date:",
        "time:",
        "venue:",
        "location:",
        "address:",
        "contact:",
        "phone:",
        "email:",
    )

    for line in lines:

        lower_line = line.lower()

        if lower_line.startswith(ignored_labels):

            continue

        if find_date(line):

            continue

        if find_time(line):

            continue

        if len(line) > 25:

            description_lines.append(line)

    if description_lines:

        return " ".join(
            description_lines
        )[:1000]

    return None


# --------------------------------------------------
# FIND CHECKLIST ITEMS
# --------------------------------------------------

def find_checklist_items(text):

    if not text:
        return []

    lines = [

        line.strip()

        for line in text.splitlines()

        if line.strip()
    ]

    tasks = []

    checklist_started = False

    checklist_labels = (

        "checklist",
        "preparation",
        "things to bring",
        "requirements",
        "before the event",
    )

    for line in lines:

        lower_line = line.lower()

        if any(
            label in lower_line
            for label in checklist_labels
        ):

            checklist_started = True

            continue

        if checklist_started:

            if lower_line.startswith(
                ("venue", "contact", "date", "time")
            ):

                checklist_started = False

                continue

            # Remove bullets and numbering
            task = re.sub(
                r"^[\-\*•●▪\d.)]+\s*",
                "",
                line
            ).strip()

            if len(task) >= 3:

                tasks.append(
                    task[:200]
                )

    # Remove duplicate tasks

    unique_tasks = []

    seen = set()

    for task in tasks:

        if task.lower() not in seen:

            unique_tasks.append(task)

            seen.add(task.lower())

    return unique_tasks
