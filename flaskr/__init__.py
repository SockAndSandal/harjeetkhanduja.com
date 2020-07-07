from flask import Flask, render_template, redirect, url_for, request, flash
from flask_mail import Mail, Message
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    emails = StringField('Email', validators = [DataRequired()])
    submit = SubmitField(' SEND ')

app = Flask(__name__)

app.secret_key = 'foobarbaz'
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'amanbeer899@gmail.com'
app.config['MAIL_PASSWORD'] = 'lightningfury'
app.config['MAIL_DEFAULT_SENDER'] = ('Harjeet Khanduja', 'amanbeer899@gmail.com')
app.config['MAIL_ASCII_ATTACHMENTS'] = False

mail = Mail(app)


@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/book/', methods = ['GET', 'POST'])
def book():
    form = LoginForm()
    if request.method == 'GET':
        return render_template('book.html', form = form)

    if request.method == 'POST':
        if form.validate_on_submit():
            flash('Thanks for your interest! Your free book preview will be sent shortly!')
            return redirect('/book')
        email = request.form['emails']
        recipients = [email]
        msg = Message('Test Mail', recipients)
        mail.send(msg)






    if form.validate_on_submit():
        flash('Thanks for your interest! Your free book preview will be sent shortly!')
        return redirect('/book') 
    email = request.form['emails']
    recipients = [email]

    msg = Message('Hello Test', recipients)
    mail.send(msg)

@app.route('/contact/')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)