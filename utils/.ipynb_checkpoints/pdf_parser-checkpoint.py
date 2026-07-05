import pdfplumber
from PyPDF2 import PdfReader


def extract_text_from_pdf(uploaded_file):
    text = ""

    try:
        with pdfplumber.open(uploaded_file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()

                if page_text:
                    text += page_text + "\n"

    except Exception:
        reader = PdfReader(uploaded_file)

        for page in reader.pages:
            text += page.extract_text()

    return text