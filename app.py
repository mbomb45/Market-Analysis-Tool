
from flask import Flask, render_template, request, send_file
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    property_name = request.form['property_name']
    location = request.form['location']
    unit_types = request.form['unit_types']
    current_rents = request.form['current_rents']

    # Generate a report
    report_content = f"Property: {property_name}\nLocation: {location}\nUnit Types: {unit_types}\nCurrent Rents: {current_rents}"
    pdf_path = generate_pdf_report(report_content)

    return render_template('results.html', property_name=property_name, location=location, pdf_path=pdf_path)

def generate_pdf_report(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Market Analysis Report", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, content)
    pdf_path = "/mnt/data/market_analysis_report.pdf"
    pdf.output(pdf_path)
    return pdf_path

@app.route('/download_report')
def download_report():
    return send_file("/mnt/data/market_analysis_report.pdf", as_attachment=True)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
