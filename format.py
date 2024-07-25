import datetime as datetime

standard_format = '%m/%d/%y'
# **************** Period Mapping ******************************
date_mapping = [
    (datetime.datetime(2024, 1, 1), datetime.datetime(2024, 1, 27)),
    (datetime.datetime(2024, 1, 28), datetime.datetime(2024, 2, 24)),
    (datetime.datetime(2024, 2, 25), datetime.datetime(2024, 3, 23)),
    (datetime.datetime(2024, 3, 24), datetime.datetime(2024, 4, 20)),
    (datetime.datetime(2024, 4, 21), datetime.datetime(2024, 5, 18)),
    (datetime.datetime(2024, 5, 19), datetime.datetime(2024, 6, 15)),
    (datetime.datetime(2024, 6, 16), datetime.datetime(2024, 7, 13)),
    (datetime.datetime(2024, 7, 14), datetime.datetime(2024, 8, 10)),
    (datetime.datetime(2024, 8, 11), datetime.datetime(2024, 9, 7)),
    (datetime.datetime(2024, 9, 8), datetime.datetime(2024, 10, 5)),
    (datetime.datetime(2024, 10, 6), datetime.datetime(2024, 11, 2)),
    (datetime.datetime(2024, 11, 3), datetime.datetime(2024, 11, 30)),
    (datetime.datetime(2024, 12, 1), datetime.datetime(2024, 12, 31))
]
# **************************************************************

def convert_period(date):
    date = datetime.datetime.strptime(date, standard_format)

    for i, (start, end) in enumerate(date_mapping):
        if start <= date <= end:
            return i + 1 
    return None

def convert_date(date):
    try:
        # Check if the date is already in standard format
        datetime.datetime.strptime(str(date), standard_format)
        return date
    except ValueError:
        # If date is not in standard format, convert it
        input_format = '%b %d, %Y'
        try:
            standard_date = datetime.datetime.strptime(date, input_format).strftime(standard_format)
            return standard_date
        except ValueError:
            # Handle cases where date format is not as expected
            return "Invalid date format"

# def convert_reference(num):
#     return num


def convert_num(num, key):
    if "Updated Reference" in key:
        standard_num = ''.join(filter(lambda x: x.isdigit() or x == '.', str(num)))
    else:
        standard_num = ''.join(filter(lambda x: x.isdigit() or x == '.' or x == '-', str(num)))
    return standard_num

 
def need_convert(key, value):
    if "Date" in key:
        return convert_date(value)
    elif "Location" in key:
        return value
    elif "Period" in key:
        return convert_period(value)
    elif "Unit" in key:
        return value
    # elif "Invoice/Reference#" in key:
    #     return convert_reference(value)
    else:
        return convert_num(value, key)
