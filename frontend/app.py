from flask import Flask
from flask import render_template
from flask import url_for
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/turnOn')
def turnOn():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.output(2, GPIO.HIGH)
    return "Lampe eingeschaltet."

@app.route('/api/turnOff')
def turnOff():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.OUT)
    GPIO.output(2, GPIO.LOW)
    return "Lampe ausgeschaltet."

@app.route('/api/toggle')
def toggle():
    #yet to implement
    return "Lampe toggled."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)