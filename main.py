from text_extract import sort_text
from parse import parse_text


pdf_file = r'C:\Users\dlam01\OneDrive - FGF Brands Inc\Desktop\projects\InvoiceDataExtractor\invoices\example.pdf'
text = sort_text(pdf_file)
parse_text(text)




    


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