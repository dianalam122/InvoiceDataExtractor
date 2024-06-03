import datetime

def need_convert(key, value):
    if key in ['Customer Number', 'Service Start Date', 'Service End Date']



def convert_date(date):
    format = '%B %d %Y'
    standard_format = '%m/%d/%y'
    standard_date = datetime.datetime.strptime(date, format).strftime(standard_format)
    print(standard_date)

date = 'April 13 2024'
convert_date(date)
