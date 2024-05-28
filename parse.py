import re
from itertools import filterfalse

#**************************** pattern dictionary *****************************
# extract numerical values ONLY 
patterns1 = {
    'Customer Number': r'\d{3}-\d{4}-\d{3}',
    'kWh Month': r'kWh Used\s*([\d,]+)',
    'Cost per Day': r'Cost per Day\s*[^0-9]*([\d.]+)',
    'Days on Bill': r'Days on Bill\s*\d{2}',
}

# extract date values ONLY
patterns2 = {
    'Billing Date': r'Billing Date:\*s\d{2}/\d{2}/\d{2}',
    'Service Start Date':r'Billing Period\s*([\D]{3}\s*\d{2},\s*\d{4})', # need match.group(1)
    'Service End Date':r'-\s*([\D]{3}\s*\d{2},\s*\d{4})' # need match.group(1)
}
#*****************************************************************************

def parse_text(text, page_index):

    data1 = {}
    data2 = {}

    if page_index == 0:
        for key, pattern in patterns1.items():
            reMatch = re.search(pattern, text) 

            if reMatch:
                match = reMatch.group(0) # entire ------> .group(1) is the first capture/group
                data1[key] = ''.join(filterfalse(str.isalpha, match))
            else: 
                data1[key] = None
        print(data1)
    elif page_index == 1:
        for key, pattern in patterns2.items():
            reMatch = re.search(pattern, text)

            if reMatch:
                match = reMatch.group(1)
                data2[key] = match
            else:
                data2[key] = None
        print(data2)

    print(data2.update(data1))
    return (data2.update(data1))


