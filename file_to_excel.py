from text_extract import sort_text
from parse import parse_text
import pandas as pd
from io import BytesIO
import os
# from openpyxl import load_workbook
from flask import send_file

# ***************************** Column Order **********************************************
columns_order = [
    'Location', 'Updated Reference', 'Invoice/Reference#', 'Units used per Month', 'Unit',
    'Cost per Day', 'Days on Bill', 'Calculated total account balance', 'Total Account Balance',
    'Total Additional Products & Services', 'Previous Bill', 'Total Current Energy Charge',
    'City Services', 'Taxes', 'Late Charges', 'Billing Date', 'Period', 'Service Start Date',
    'Service End Date'
]
# *****************************************************************************************


# gets df from singular pdf file
def get_df(pdf_file):
    # Extracts text from pdf horizontally
    text = sort_text(pdf_file)

    # dict -> df 
    invoice_dict = parse_text(text)
    invoice_df = pd.DataFrame([invoice_dict])
    
    invoice_df = invoice_df[columns_order]

    return invoice_df

def write_to_excel(df, action, ROOT, upload_folder):
    
    output = BytesIO()
    # Create a Pandas Excel writer
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

        # writer.close()
        output.seek(0)
        
    if action == 'append':
        # append df to root
        root_df = pd.read_excel(ROOT)
        combined_df_list = [root_df, df]
        combined_df = pd.concat(combined_df_list)

        # Write the combined data back to the root file
        with pd.ExcelWriter(ROOT, engine='xlsxwriter') as writer:
            combined_df.to_excel(writer, sheet_name='Sheet1', index=False)
    else:
        # write the new data to a new file
        excel = output.getvalue()

        return send_file(
            BytesIO(excel),
            download_name = 'extracted_data.xlsx',
            as_attachment = True,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )    
    clear_upload_folder(upload_folder)


def pdfs_to_acc_df(folder):
    # list of pdfs -> acc df
    acc_df = pd.DataFrame()

    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        df = get_df(file_path)
        acc_df = pd.concat([acc_df, df], ignore_index=True)

    return acc_df


def make_excel(upload_folder, action, ROOT):
    acc_df = pdfs_to_acc_df(upload_folder)
    return write_to_excel(acc_df, action, ROOT, upload_folder)





