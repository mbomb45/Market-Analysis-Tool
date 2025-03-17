
from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os

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
    upgrades = request.form.getlist('upgrades')

    # Process data and calculate ROI (basic example)
    rent_increase = len(upgrades) * 50  # Assume $50 rent increase per upgrade
    upgrade_cost = len(upgrades) * 1500  # Assume $1500 per upgrade
    roi = (rent_increase * 12) / upgrade_cost * 100 if upgrade_cost > 0 else 0
    payback_period = upgrade_cost / (rent_increase * 12) if rent_increase > 0 else "N/A"

    report_content = f"""Property: {property_name}
Location: {location}
Unit Types: {unit_types}
Current Rents: {current_rents}
Upgrades Selected: {', '.join(upgrades)}
Estimated Rent Increase: ${rent_increase}
ROI: {roi:.2f}%
Payback Period: {payback_period} years"""

    pdf_path = generate_pdf_report(report_content)

    return render_template('results.html', property_name=property_name, location=location, rent_increase=rent_increase, roi=roi, pdf_path=pdf_path)

def generate_pdf_report(content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Market Analysis Report", ln=True, align='C')
    pdf.ln(10)
    pdf.multi_cell(0, 10, content)

    pdf_path = "market_analysis_report.pdf"
    pdf.output(pdf_path)
    
    return pdf_path

@app.route('/download_report')
def download_report():
    return send_file("market_analysis_report.pdf", as_attachment=True)

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
