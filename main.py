import os
from flask import Flask, render_template, request, send_file
from file_to_excel import make_excel
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
        # Gets the list of files
        for uploaded_file in request.files.getlist('file'):
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))

        excel_data = make_excel(app.config['UPLOAD_FOLDER'])
        clear_upload_folder()

        return send_file(
            BytesIO(excel_data),
            download_name = 'extracted_data.xlsx',
            as_attachment = True,
            mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    return render_template('index.html')

# remove files under uploads folder
def clear_upload_folder():
    for file in os.listdir(UPLOAD_FOLDER):
        file_path = os.path.join(UPLOAD_FOLDER, file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    app.run(debug=True)

