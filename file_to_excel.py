from text_extract import sort_text
from parse import parse_text
import pandas as pd
from io import BytesIO

# ***************************** Column Order **********************************************
columns_order = [
    'Location', 'Updated Reference', 'Invoice/Reference#', 'Units used per Month', 'Unit',
    'Cost per Day', 'Days on Bill', 'Calculated total account balance', 'Total Account Balance',
    'Total Additional Products & Services', 'Previous Bill', 'Total Current Energy Charge',
    'City Services', 'Taxes', 'Late Charges', 'Billing Date', 'Period', 'Service Start Date',
    'Service End Date'
]
# *****************************************************************************************


def get_df(pdf_file):
    # Extracts text from pdf horizontally
    text = sort_text(pdf_file)

    # dict -> df 
    invoice_dict = parse_text(text)
    invoice_df = pd.DataFrame([invoice_dict])
    
    invoice_df = invoice_df[columns_order]
    return invoice_df


def make_excel(df):
    # Create a Pandas Excel writer
    output = BytesIO()

    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:

        # Convert to Excel object
        df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=1, header=False)
        # Get the xlsxwriter workbook and worksheet objects.
        workbook = writer.book
        worksheet = writer.sheets['Sheet1']

        # Header format
        header_format = workbook.add_format(
            {
                'bold': True,
                'text_wrap': True,
                'valign': "top",
                'border': 1,
            }
        )

        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)

        writer.close()
        output.seek(0)
    return output.getvalue()









