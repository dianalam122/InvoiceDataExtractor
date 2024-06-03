import datetime

def convert_date(date):
    standard_format = '%m/%d/%y'
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

def convert_num(num):
    standard_num = ''.join(filter(lambda x: x.isdigit() or x == '.', str(num)))
    return standard_num

def need_convert(key, value):
    if "Date" in key:
        return convert_date(value)
    else:
        return convert_num(value)
