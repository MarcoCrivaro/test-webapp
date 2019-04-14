from flask import Flask
from flask import render_template
from flask import url_for
#import RPi.GPIO as GPIO
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/turnOn')
def turnOn():
    #GPIO.setPin(pinNumber, ON)
    print("turn on lamp")
    return "Lampe eingeschaltet."

@app.route('/api/turnOff')
def turnOff():
    #GPIO.setPin(pinNumber, ON)
    return "Lampe ausgeschaltet."

@app.route('/api/toggle')
def toggle():
    #GPIO.setPin(pinNumber, ON)
    return "Lampe toggled."