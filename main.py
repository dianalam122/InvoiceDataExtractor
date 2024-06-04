from text_extract import sort_text
from parse import parse_text
import pandas as pd
import xlsxwriter
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Gets the list of files from webpage
        file_list = request.files.getlist("file")

        # Iterate for reach file in list
        for file in file_list:
            file.save(file.filename)
        return "Files uploaded Sucessfully!"

if __name__ == '__main__':
    app.debug = True
    app.run()
    app.run(debug = True)



# pdf_file = r'C:\Users\dlam01\OneDrive - FGF Brands Inc\Desktop\projects\InvoiceDataExtractor\invoices\example.pdf'

# # Extracts text from pdf horizontally
# text = sort_text(pdf_file)

# # Returns dict -> df 
# invoice_dict = parse_text(text)
# invoice_df = pd.DataFrame([invoice_dict])



# # Create a Pandas Excel writer
# file_name = 'example.xlsx'
# writer = pd.ExcelWriter(file_name, engine='xlsxwriter')
# # Convert to Excel object
# invoice_df.to_excel(writer, sheet_name='Sheet1', index=False, startrow=1, header=False)
# # Get the xlsxwriter workbook and worksheet objects.
# workbook = writer.book
# worksheet = writer.sheets['Sheet1']

# # Header format
# header_format = workbook.add_format(
#     {
#         'bold': True,
#         'text_wrap': True,
#         'valign': "top",
#         'border': 1,
#     }
# )

# for col_num, value in enumerate(invoice_df.columns.values):
#     worksheet.write(0, col_num, value, header_format)

# writer.close()











# other info:
#     period:
#     vendor account: user input cannot extract from image
#     service period (service end - service start + 1)
#         make note if different than "days on bill"
