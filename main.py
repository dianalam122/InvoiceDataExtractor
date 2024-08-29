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

    uploaded_file_root = request.files.get('root-file')
    if uploaded_file_root:
        temp_dir = r'InvoiceDataExtractor\temp_dir'
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
    
    file_path_root = os.path.join(temp_dir, uploaded_file_root.filename)
    uploaded_file_root.save(file_path_root)
    ROOT = os.path.abspath(file_path_root  )

    if request.method == 'POST':
        # Gets the list of files
        for uploaded_file in request.files.getlist('file'):
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], uploaded_file.filename))

        return make_excel(app.config['UPLOAD_FOLDER'], action, ROOT, UPLOAD_FOLDER)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

