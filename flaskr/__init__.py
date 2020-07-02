from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/book/')
def book():
    return render_template("book.html")

@app.route('/contact/')
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)