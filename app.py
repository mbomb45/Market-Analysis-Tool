
from flask import Flask, request, jsonify
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def home():
    return "Market Analysis Tool is Running!"

if __name__ == '__main__':
    app.run(debug=True)
