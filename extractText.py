import fitz
import pytesseract
from PIL import Image
import io

# Extract text from PDF 
#   extracts: address
def extract_text(sample_pdf):
    pdf_doc = fitz.open(sample_pdf)
    text = ""
    for page_num in range(2):
        page = pdf_doc[page_num]
        text += page.get_text()

    return text

# Extract text from img object of PDF
#   extracts: 
def extract_text_from_image(sample_pdf):
    pdf_doc = fitz.open(sample_pdf)
    text = ""
    for page_num in range(2):
        page = pdf_doc[page_num]
        # image object of pdf
        pix = page.get_pixmap()
        img = Image.open(io.BytesIO(pix.tobytes()))
        text += pytesseract.image_to_string(img)
    return text


