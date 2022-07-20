from flask import Flask, render_template, url_for, flash, redirect
from flask_behind_proxy import FlaskBehindProxy


app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '2a0d5392c1401e477b16268f3586cc07'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
