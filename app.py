from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    property_name = request.form['property_name']
    location = request.form['location']
    return f"Received data for {property_name} in {location}"

if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=10000)
