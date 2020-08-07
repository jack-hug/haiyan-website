from flask import flash,redirect,url_for,render_template
from . import app,db
from .models import Message
from .forms import MessageForm

def formSubmit():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        email = form.email.data
        message = Message(name = name, body = body, email = email)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to admin!')
    else:
        flash('The information you entered is incorrect!')

@app.route('/messages')
def messages():
    messages = Message.query.order_by(Message.timestamp.asc()).all()
    return render_template('messages.html',messages = messages)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Contact',methods = ['GET', 'POST'])
def contact():
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        email = form.email.data
        message = Message(name = name, body = body, email = email)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to admin!')
    else:
        flash('The information you entered is incorrect!')
        
    return render_template('contact.html',form = form)

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
    return render_template('injection_mold.html')

@app.route('/Stamping_die')
def stamping_die():
    return render_template('stamping_die.html')

@app.route('/Hot_runner')
def hot_runner():
    return render_template('hot_runner.html')