from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    emails = StringField('Email', validators = [DataRequired()])
    submit = SubmitField(' SEND ')

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'no-reply@harjeetkhanduja.com'
app.config['MAIL_PASSWORD'] = 'abcd@1234'
app.config['MAIL_DEFAULT_SENDER'] = ('Harjeet Khanduja', 'no-reply@harjeetkhanduja.com')
app.config['MAIL_ASCII_ATTACHMENTS'] = False
app.config['DEBUG'] = False
app.secret_key = 'foobarbaz'
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

mail = Mail(app)


@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/book/nab', methods = ['GET', 'POST'])
def nab():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('nab.html', form = form)

    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Thanks for your interest! Your free book preview will be sent shortly!')
            return redirect('/book')
        email = request.form['emails']
        recipients = [email]
        msg = Message('Nothing About Business: Preview', recipients)
        msg.body = "Greetings Reader! Thank you for your interest in Harjeet's first collection of stories, Nothing about Business! Illustrating strategies for attracting and engaging the audience with real-life business stories, this title is simple, practical and inspiring. Some of the topics covered in the book include Recruitment, Self and Work Management and Leadership. This book is available on Amazon, check it out at the link below: [https://www.amazon.com/dp/B08CNG6VR5](https://www.amazon.com/dp/B08CNG6VR5). To help your purchasing decision a little bit, here's a preview for you to peruse in your free time!"
        with app.open_resource("Nothing About Business_Preview.pdf") as fp:
            msg.attach("Nothing About Business_Preview.pdf", "application/pdf", fp.read())
        mail.send(msg)

@app.route('/book/tuktuk')
def tuktuk():
    return render_template("tuktuk.html")

@app.route('/book/storytelling_leader')
def storytelling():
    return render_template("storytelling_leader.html")

@app.route('/book/how_leaders_decide')
def leaders():
    return render_template("leaders.html")

@app.route('/book/ldb')
def ldb():
    return render_template("ldb.html")

@app.route('/blog')
def blog():
    return redirect('http://blog.harjeetkhanduja.com/')

@app.route('/contact/')
def contact():
    return render_template("contact.html")