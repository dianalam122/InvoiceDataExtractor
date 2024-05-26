import re
from rePatterns import patterns


def parse_text(text):
    data = {}

    for key, pattern in patterns.items():
        match = re.search(pattern, text)

        if match:
            data[key] = match.group(1) #returns text that matched first capturing group
        else: 
            data[key] = None

    return data

