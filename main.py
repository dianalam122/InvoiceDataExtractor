from text_extract import process_image
from parse import parse_text
from pdf2image import convert_from_path
import os

sample_pdf = 'invoices/real.pdf'

pages = convert_from_path(sample_pdf, first_page=1, last_page=1)  # Only extract the first page
first_page_image = 'first_page.jpg'
pages[0].save(first_page_image, 'JPEG')
# process_image(first_page_image)

# parse text for specifics
first_page_text = process_image(first_page_image)
parse_text(first_page_text)
os.remove(first_page_image)




#_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
# second page doc

# pages = convert_from_path(sample_pdf, first_page=2, last_page=2)
# second_page_image = 'second_page.jpg'
# pages[0].save(second_page_image, 'JPEG')
# process_image(second_page_image)
# os.remove(second_page_image)





# parsed_text = parse_text(pdf_text)


# need: 
# extract directly from doc:
#     location
#     cps account
#     kwh used (maybe do ccp too with user input)
#     units (user input)
#     cost per day
#     billing date (store month separately)
#     service end date
#     service start date
#     days on bill


# other info:
#     period: user input (or look into fgf period schedule)
#     vendor account: user input
#     invoice/reference number: format -> cps acount (no dash) - Month
#     service period (service end - service start + 1)
#         make note if different than "days on bill"

