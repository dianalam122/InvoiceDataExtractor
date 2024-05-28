import re

#**************************** pattern dictionary *****************************
# extract date values ONLY
patterns2 = {
    'Service Start Date':r'Billing Period\s*\D{3}\s*\d{2}', # need match.group(1)
    # 'Service End Date': ''
}
#*****************************************************************************

text_path = 'outputs/output_second_page'

with open(text_path, 'r') as file:
    text = file.read()


def parse_text(text):
    data2 = {}

    for key, pattern in patterns2.items():
        reMatch = re.search(pattern, text)

        if reMatch:
            match = reMatch.group(1)
            data2[key] = match
        else:
            data2[key] = None
    print(data2)

parse_text(text_path)

