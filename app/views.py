from flask import flash,redirect,url_for,render_template,session
from . import app,db


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Contact')
def contact():
    return render_template('contact.html')

@app.route('/Company')
def company():
    return render_template('company.html')

@app.route('/Mold_base')
def mold_base():
    return render_template('mold_base.html')

@app.route('/Customized')
def customized():
    return render_template('customized.html')

@app.route('/Injection_mold')
def injection_mold():
    return render_template('injection_mold.html',set_tab=1)

@app.route('/Stamping_die')
def stamping_die():
    return render_template('stamping_die.html')

@app.route('/Hot_runner')
def hot_runner():
    return render_template('hot_runner.html')