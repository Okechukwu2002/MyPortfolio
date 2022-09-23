from flask import *
from flask_sqlalchemy import *
from werkzeug.security import *


app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SECRET_KEY'] = 'hshshhdjghs'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.String(500), nullable=False)

    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message



@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        content = Message(name=name, email=email, subject=subject, message=message)
        try:
            db.session.add(content)
            db.session.commit()
            flash('Thank you for your message')
            return redirect(url_for('index'))
        except:
            flash('Your message was not sent, please resend')

    return render_template('index.html')


@app.route('/bluemode', methods=['POST','GET'])
def bluemode():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        content = Message(name=name, email=email, subject=subject, message=message)
        try:
            db.session.add(content)
            db.session.commit()
            flash('Thank you for your message')
            return redirect(url_for('bluemode'))
        except:
            flash('Your message was not sent, please resend')

    return render_template('bluemode.html')


@app.route('/greenmode', methods=['POST','GET'])
def greenmode():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        content = Message(name=name, email=email, subject=subject, message=message)
        try:
            db.session.add(content)
            db.session.commit()
            flash('Thank you for your message')
            return redirect(url_for('greenmode'))
        except:
            flash('Your message was not sent, please resend')

    return render_template('greenmode.html')


@app.route('/purplemode', methods=['POST','GET'])
def purplemode():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        content = Message(name=name, email=email, subject=subject, message=message)
        try:
            db.session.add(content)
            db.session.commit()
            flash('Thank you for your message')
            return redirect(url_for('purplemode'))
        except:
            flash('Your message was not sent, please resend')

    return render_template('purplemode.html')
