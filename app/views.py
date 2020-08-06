from flask import flash,redirect,url_for,render_template,session
from . import app,db
from .models import Message
from .forms import MessageForm


@app.route('/', methods = ['GET', 'POST'])
def index():
    global form
    form = MessageForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        email = form.email.data
        message = Message(body = body, name = name, email = email)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to admin!')
        return redirect(url_for('index'))
    
    return render_template('index.html',form = form)

@app.route('/Contact')
def contact():
    return render_template('contact.html',form = form)

@app.route('/Company')
def company():
    return render_template('company.html',form = form)

@app.route('/Mold_base')
def mold_base():
    return render_template('mold_base.html',form = form)

@app.route('/Customized')
def customized():
    return render_template('customized.html',form = form)

@app.route('/Injection_mold')
def injection_mold():
    return render_template('injection_mold.html',set_tab=1,form = form)

@app.route('/Stamping_die')
def stamping_die():
    return render_template('stamping_die.html',form = form)

@app.route('/Hot_runner')
def hot_runner():
    return render_template('hot_runner.html',form = form)