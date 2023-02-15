from docx import Document
from docxtpl import DocxTemplate

from flask import Flask, request, send_file

app = Flask(__name__)

@app.route('/')
def home():
    client_name = request.args.get('client_name')
    contract_price = request.args.get('contract_price')
    contact_phone = request.args.get('contact_phone')

    doc = DocxTemplate('templ.docx')

    context = {
        'client_name': client_name,
        'contract_price': contract_price,
        'contact_phone': contact_phone,
    }

    doc.render(context)
    doc.save('output.docx')

    return send_file('output.docx')

if __name__ == '__main__':
    app.run(debug=True)



