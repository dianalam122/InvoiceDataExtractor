from text_extract import sort_text
from parse import parse_text
from clean import clear_upload_folder
import pandas as pd
from io import BytesIO
import os
from flask import send_file
import openpyxl


# ***************************** Column Order **********************************************
columns_order = [
    'Location', 'Vendor Code', 'Updated Reference', 'Invoice/Reference #', 'Units used per Month', 'Unit',
    'Cost per Day', 'Days on Bill', 'Calculated Total Account Balance', 'Total Account Balance',
    'Total Additional Products & Services', 'Previous Bill', 'Total Current Energy Charge',
    'City Services', 'State & Local Sales Taxes', 'Late Charges', 'Billing Date', 'Period', 'Service Start Date',
    'Service End Date'
]
# *****************************************************************************************

# ***************************** Header Styling *************************************

def header_format(writer, df):

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

# ***************************************************************************

# gets df from singular pdf file
def get_df(pdf_file):
    # Extracts text from pdf horizontally
    text = sort_text(pdf_file)

    # dict -> df 
    invoice_dict = parse_text(text)
    invoice_df = pd.DataFrame([invoice_dict])
    
    invoice_df = invoice_df[columns_order]

    return invoice_df

def standardize_cols(df):
    # Convert column names to lower case and strip spaces
    # df.columns = df.columns.str.strip().str.lower()
    return df

def write_to_excel(df, action, ROOT, UPLOAD_FOLDER):
    
    output = BytesIO()

    if action == 'append':
        df = standardize_cols(df)
        # append df to root
        root_df = pd.read_excel(ROOT)
        root_df = standardize_cols(root_df)

        combined_df = pd.concat([root_df, df])

        # save to ROOT excel
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            combined_df.to_excel(writer, sheet_name='Sheet1', index=False)
            header_format(writer, combined_df)
            output.seek(0)
    else:
        # Create a Pandas Excel writer
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            # Convert to Excel object
            df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=1, header=False)
            header_format(writer, df)
            output.seek(0)
    
    excel = output.getvalue()

    clear_upload_folder(UPLOAD_FOLDER) 

    return send_file(
        BytesIO(excel),
        download_name = 'extracted_data.xlsx',
        as_attachment = True,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )    



def pdfs_to_acc_df(folder):
    # list of pdfs -> acc df
    acc_df = pd.DataFrame()

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        df = get_df(file_path)
        acc_df = pd.concat([acc_df, df], ignore_index=True)

    return acc_df


def make_excel(upload_folder, action, ROOT, UPLOAD_FOLDER):
    acc_df = pdfs_to_acc_df(upload_folder)
    return write_to_excel(acc_df, action, ROOT, UPLOAD_FOLDER)



