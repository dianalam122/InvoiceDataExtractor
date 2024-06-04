from text_extract import sort_text
from parse import parse_text
import pandas as pd
import xlsxwriter

def get_df(pdf_file):
    # Extracts text from pdf horizontally
    text = sort_text(pdf_file)

    # Returns dict -> df 
    invoice_dict = parse_text(text)
    invoice_df = pd.DataFrame([invoice_dict])

    return invoice_df


def make_excel(df):
    # Create a Pandas Excel writer
    file_name = 'example.xlsx'
    writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
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







