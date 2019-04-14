from flask import Flask
from flask import render_template
from flask import url_for
app = Flask(__name__)

with app.test_request_context():
    url_for('static', filename='style.css')

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api')
def api():
    return "Api Endpoint"