from flask import Flask, render_template, request, send_file
from pdf2docx import Converter
#Updated
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    if 'pdf_file' not in request.files:
        return "No file part"

    pdf_file = request.files['pdf_file']
    if pdf_file.filename == '':
        return "No selected file"

    pdf_filename = pdf_file.filename
    pdf_path = f"uploads/{pdf_filename}"
    pdf_file.save(pdf_path)

    docx_path = f"uploads/{pdf_filename.split('.')[0]}.docx"

    cv = Converter(pdf_path)
    cv.convert(docx_path, start=0, end=None)
    cv.close()

    return send_file(docx_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
