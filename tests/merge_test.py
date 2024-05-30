
data1 = {'Customer Number': '300-5102-932',
        'kWh Month': '1,783',
        'Cost per Day': '6.42',
        'Days on Bill': '32',
        'Billing Date': '05/15/24'}

data2 = {'Service Start Date': 'Apr 12, 2024',
        'Service End Date': 'May 13, 2024'}

def data_merge(data1, data2):
    result = {**data1, **data2}
    print(result)
    return result


# entry pt
print(data1)
print(data2)
data_merge(data1, data2)

