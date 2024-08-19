import os
from flask import Flask, render_template, request
from file_to_excel import make_excel


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
    action = request.form['action']
    ROOT = request.files.get('root-file')
    if request.method == 'POST':
        # Gets the list of files
        for uploaded_file in request.files.getlist('file'):
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))

        return make_excel(app.config['UPLOAD_FOLDER'], action, ROOT, UPLOAD_FOLDER)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

