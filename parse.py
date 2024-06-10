import re
from format import need_convert

#**************************** pattern dictionary *****************************
patterns = {
    'Location': r'FGF LLC Customer Number:.*\n(.*)',
    'Customer Number': r'Customer Number:\s*([^\s]+)',
    'Units used per Month': r'[^0-9\s]+\s*Used\s*([\d,]+)',
    'Unit': r'([^0-9\s]+)\s*Used',
    'Cost per Day': r'Cost per Day\s*[^0-9]*([\d.]+)',
    'Days on Bill': r'Days on Bill\s*(\d{2})',
    'Total per Invoice': r'(?:Total Account Balance|Total Additional Products & Services)\s*[^0-9]*([\d.,]+)',
    'Total Current Energy Charge': r'Total Current Energy Charge\s*[^0-9]*([\d.,]+)',
    'City Services': r'City Services\s*[^0-9]*([\d.]+)',
    'Taxes': r'State & Local Sales Taxes\s*[^0-9]*([\d.,]+)',
    'Payments & Adjustments': r'Subtotal\s*[^0-9]*([\d.,]+)',
    'Billing Date': r'Billing Date:\s*(\d{2}/\d{2}/\d{2})',
    'Period': r'Billing Date:\s*(\d{2}/\d{2}/\d{2})',
    'Service Start Date': r'Billing Period\s*([^0-9]{3}\s*\d{2},\s*\d{4})',
    'Service End Date': r'Billing Period\s*[^0-9]{3}\s*\d{2},\s*\d{4}\s*-\s*([^0-9]{3}\s*\d{2},\s*\d{4})'
}
#*****************************************************************************

def parse_text(text):
    data = {}
    for key, pattern in patterns.items():
        reMatch = re.search(pattern, text)
        if reMatch:
            match = reMatch.group(1)
            # Standard formatting 
            value = need_convert(key, match)
            data[key] = value
        else:
            data[key] = None
    # print(data)
    return data




















