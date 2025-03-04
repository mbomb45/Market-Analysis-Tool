
from flask import Flask, request, jsonify
from fpdf import FPDF

app = Flask(__name__)

@app.route('/')
def home():
    return "Market Analysis Tool is Running!"

if __name__ == '__main__':
app.run(host="0.0.0.0", port=10000, debug=True)
