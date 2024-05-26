import fitz


# Extract text from first two pages of PDF
def extract_text(sample_pdf):
    pdf_doc = fitz.open(sample_pdf)
    text = ""
    for page_num in range(2):
        page = pdf_doc[page_num]
        text += page.get_text()

    return text


sample_pdf = "invoices/sample.pdf"
print(extract_text(sample_pdf))


# Parse through text
