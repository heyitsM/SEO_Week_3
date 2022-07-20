from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
from flask_behind_proxy import FlaskBehindProxy


app = Flask(__name__)
proxied = FlaskBehindProxy(app)
app.config['SECRET_KEY'] = '2a0d5392c1401e477b16268f3586cc07'


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

@app.route("/register")
@app.route("/r")
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit(): # checks if entries are valid
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('login')) # if so - send to home page
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
@app.route("/l")
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login successful for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
