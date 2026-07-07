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
        # Rewind the file stream back to the start (byte 0)
        uploaded_file.seek(0)
        
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text