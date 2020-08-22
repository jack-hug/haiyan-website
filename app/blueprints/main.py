from flask import flash,redirect,url_for,render_template,Blueprint
from ..extensions import db
from ..models import Message
from ..forms import MessageForm

main = Blueprint('main', __name__)


# def formSubmit():
#     form = MessageForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         body = form.body.data
#         email = form.email.data
#         message = Message(name = name, body = body, email = email)
#         db.session.add(message)
#         db.session.commit()
#         flash('Your message have been sent to admin!')
#     else:
#         flash('The information you entered is incorrect!')

@main.route('/messages')
def messages():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('main/messages.html',messages = messages)

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/Contact',methods = ['GET', 'POST'])
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
        return redirect(url_for('main.contact'))
        
    return render_template('main/contact.html',form = form)

@main.route('/Company')
def company():
    return render_template('main/company.html')

@main.route('/Mold_base')
def mold_base():
    return render_template('main/mold_base.html')

@main.route('/Customized')
def customized():
    return render_template('main/customized.html')

@main.route('/Injection_mold')
def injection_mold():
    return render_template('main/injection_mold.html')

@main.route('/Stamping_die')
def stamping_die():
    return render_template('main/stamping_die.html')

@main.route('/Hot_runner')
def hot_runner():
    return render_template('main/hot_runner.html')