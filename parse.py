import re
from format import need_convert

#**************************** Pattern Dictionary ****************************************
patterns = {
    'Location': r'FGF LLC Customer Number:.*\n(.*)',
    'Updated Reference': r'Customer Number:\s*([^\s]+)',
    'Invoice/Reference#': r'Customer Number:\s*([^\s]+)',
    'Units used per Month': r'[^0-9\s]+\s*Used\s*([\d,]+)',
    'Unit': r'([^0-9\s]+)\s*Used',
    'Cost per Day': r'Cost per Day\s*[^0-9]*([\d.]+)',
    'Days on Bill': r'Days on Bill\s*(\d{2})',
    'Total Account Balance': r'Total Account Balance\s*[^0-9]*([\d.,]+)',
    'Total Additional Products & Services': r'Total Additional Products & Services\s*[^0-9]*([\d.,]+)',
    'Previous Bill': r'Previous Bill\s*(-?\$[\d.,]+)',
    'Total Current Energy Charge': r'Total Current Energy Charge\s*[^0-9]*([\d.,]+)',
    'City Services': r'City Services\s*[^0-9]*([\d.]+)',
    'Taxes': r'State & Local Sales Taxes\s*[^0-9]*([\d.,]+)',
    'Late Charges':r'Late Charge \d{2}/\d{2}/\d{2}\s*(-?\$[\d.,]+)',
    'Billing Date': r'Billing Date:\s*(\d{2}/\d{2}/\d{2})',
    'Period': r'Billing Date:\s*(\d{2}/\d{2}/\d{2})',
    'Service Start Date': r'Billing Period\s*([^0-9]{3}\s*\d{2},\s*\d{4})',
    'Service End Date': r'Billing Period\s*[^0-9]{3}\s*\d{2},\s*\d{4}\s*-\s*([^0-9]{3}\s*\d{2},\s*\d{4})'
}
# *****************************************************************************************

def parse_text(text):
    data = {}
    # components of calculated Total Account Balance
    calculated_total_components = {
        'Previous Bill': 0.0,
        'Total Current Energy Charge': 0.0,
        'Total Additional Products & Services': 0.0,
        'City Services': 0.0,
        'Late Charges': 0.0,
        'Taxes': 0.0
    }

    for key, pattern in patterns.items():
        reMatch = re.search(pattern, text)
        if reMatch:
            match = reMatch.group(1)
            # Standard formatting 
            value = need_convert(key, match)
            data[key] = value
            if key in calculated_total_components:
                calculated_total_components[key] = float(value)

        else:
            data[key] = None
    # print(data)
    calculated_total = sum(calculated_total_components.values())
    data['Calculated total account balance'] = calculated_total

    return data















