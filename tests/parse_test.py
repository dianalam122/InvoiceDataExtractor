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

    data1 = {}
    data2 = {}

    if page_index == 0:
        for key, pattern in patterns1.items():
            reMatch = re.search(pattern, text) 

            if reMatch:
                match = reMatch.group(1) 
                # data1[key] = ''.join(filterfalse(str.isalpha, match))
                data1[key] = match
            else: 
                data1[key] = None
        print(data1)
        return data1
    elif page_index == 1:
        for key, pattern in patterns2.items():
            reMatch = re.search(pattern, text)

            if reMatch:
                if key == 'Service Start Date':
                    match = reMatch.group(1)
                else:
                    match = reMatch.group(2)
                data2[key] = match
            else:
                data2[key] = None
        print(data2)
        return data2

file_path = 'outputs/output_real.txt'

try: 
    with open(file_path, 'r') as file:
        file_content = file.read()
except FileNotFoundError:
    print(f'{file_path} could not be opened')

# 
parse_text(file_content, 0)


# def merge_data(data1, data2):
#     merged_data = data2.update(data1)
#     return merged_data

