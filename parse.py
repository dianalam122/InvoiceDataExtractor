import re
# from itertools import filterfalse

#**************************** pattern dictionary *****************************
# extract numerical values ONLY 
patterns1 = {
    'Customer Number': r'(\d{3}-\d{4}-\d{3})',
    'kWh Month': r'kWh Used\s*([\d,]+)',
    'Cost per Day': r'Cost per Day\s*[^0-9]*([\d.]+)',
    'Days on Bill': r'Days on Bill\s*(\d{2})',
    'Billing Date': r'Billing Date:\s*(\d{2}/\d{2}/\d{2})'
}
# extract date values ONLY
patterns2 = {
    'Service Start Date':r'Billing Period\s*([\D]{3}\s*\d{2},\s*\d{4})\s*([\D]{3}\s*\d{2},\s*\d{4})',
    'Service End Date':r'Billing Period\s*([\D]{3}\s*\d{2},\s*\d{4})\s*([\D]{3}\s*\d{2},\s*\d{4})'
}
#*****************************************************************************

def parse_text(text, page_index):
    data = {}

    if page_index == 0:
        for key, pattern in patterns1.items():
            reMatch = re.search(pattern, text) 

            if reMatch:
                match = reMatch.group(1)
                # data1[key] = ''.join(filterfalse(str.isalpha, match))
                data[key] = match
            else: 
                data[key] = None
        return data
    elif page_index == 1:
        for key, pattern in patterns2.items():
            reMatch = re.search(pattern, text)

            if reMatch:
                if key == 'Service Start Date':
                    match = reMatch.group(1)
                else:
                    match = reMatch.group(2)
                data[key] = match
            else:
                data[key] = None
        return data
    
