import os
import pandas as pd
from flask import Flask, render_template, request
from file_to_excel import get_df, make_excel
from werkzeug.utils import secure_filename

app = Flask(__name__)

DEFAULT_UPLOAD_FOLDER = 'uploads'
UPLOAD_FOLDER = os.path.join(app.root_path, DEFAULT_UPLOAD_FOLDER)
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
        convert_files_to_excel()    
        return "Files uploaded Sucessfully!"
    return render_template('index.html')


def convert_files_to_excel():
    # Convert file in uploads to excel
    acc_df = pd.DataFrame()

    for file in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file)
        df = get_df(file_path)
        acc_df = pd.concat([acc_df, df], ignore_index=True)
    # Make excel
    make_excel(acc_df)


if __name__ == '__main__':
    app.run(debug=True)

