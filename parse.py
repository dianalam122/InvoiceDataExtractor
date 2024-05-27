import re

# date_pattern = r'\d{2}/\d{2}/\d{2}'
# account_pattern = r'\d{3}-\d{4}-\d{3}'
# kwh_used_pattern = r'\d+'
# kwh_per_day_pattern = r'\d+(?:\.\d+)?'

# pattern dictionary
patterns = {
    'Billing Date': r'\d{2}/\d{2}/\d{2}',

    # 'Customer Number': r'\d{3}-\d{4}-\d{3}',
    # 'kWh Month': r'kWh Used\s*(\d+)',
    # 'kWh Day': r'Cost per Day \$([\d.]+)'

    # 'Days on Bill':
    # 'Billing Date':
    # 'Service End Date':
    # 'Service Start Date':
}

def parse_text(text):
    data = {}

    for key, pattern in patterns.items():
        match = re.search(pattern, text)

        if match:
            data[key] = match # match.group(1) returns text that matched first capturing group
        else: 
            data[key] = None
    print(data)
    return data

