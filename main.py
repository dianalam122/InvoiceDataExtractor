from extractText import extract_text, extract_text_from_image
from parse import parse_text


sample_pdf = "invoices/sample.pdf"

pdf_text = extract_text(sample_pdf)
# pdf_text = extract_text_from_image(sample_pdf)
print(pdf_text)

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

