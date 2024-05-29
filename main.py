from text_extract import process_image
from parse import parse_text
from pdf2image import convert_from_path
import os

sample_pdf = 'invoices/real.pdf'

pages = convert_from_path(sample_pdf, first_page=1, last_page=2)


for i, page in enumerate(pages):
    page_image = f'page{i + 1}.jpg'
    pages[i].save(page_image, 'JPEG')
    parse_text(process_image(page_image), i)
    os.remove(page_image)
    


# other info:
#     period:
#     vendor account: user input cannot extract from image
#     invoice/reference number: format -> cps acount (no dash) - Month
#     service period (service end - service start + 1)
#         make note if different than "days on bill"


# Qs:
#  - request access to python
#  - period start - end dates
#  - formatting? what info need? 
#  - 