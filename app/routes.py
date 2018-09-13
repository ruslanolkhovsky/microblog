from flask import render_template
from flask import request
from flask import flash
from flask import redirect
from flask import url_for

# import modules form utils folder
import sys
sys.path.insert(0, 'utils')
from simplecalc import SimpleCalc

from app import app
from app.forms import CalcForm
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)

@app.route("/calc/", methods=['GET', 'POST'])
def calc():
    form = CalcForm()
    # Check if form submit
    if form.validate_on_submit():
        # send flash message back to the form
        flash(str(SimpleCalc(form.expression.data)))
        # redirect to the result page
        return redirect('/calc')

    # otherwise return the form itself
    return render_template('calc.html', title='Calculator', form=form)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)
