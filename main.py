import os
import pandas as pd
from flask import Flask, render_template, request, send_file
from file_to_excel import get_df, make_excel
from werkzeug.utils import secure_filename
from io import BytesIO

app = Flask(__name__, static_folder='InvoiceDataExtractor/output')

UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Gets the list of files from webpage
        for uploaded_file in request.files.getlist('file'):
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))
        # convert_files_to_excel()

        excel_data = convert_files_to_excel()

        # remove files under uploads folder
        clear_upload_folder()

        return send_file(
            BytesIO(excel_data),
            download_name = 'invoices.xlsx',
            as_attachment = True,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    return render_template('index.html')

def clear_upload_folder():
    for file in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Error: {e}')


def convert_files_to_excel():
    # Convert file in uploads to excel
    acc_df = pd.DataFrame()

    for file in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file)
        df = get_df(file_path)
        acc_df = pd.concat([acc_df, df], ignore_index=True)
    # Make excel
    return make_excel(acc_df)


if __name__ == '__main__':
    app.run(debug=True)

