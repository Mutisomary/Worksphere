from flask import render_template, flash, redirect
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    employees = [
        {
            'id': 1,
            'Name': 'Mary Mutiso',
            'ContactInformation': '0792566007',
            'Position': 'Software Developer',
            'Department': 'Engineering'
        },
        {
            'id': 2,
            'Name': 'Kelvin Mutiso',
            'ContactInformation': '079256227',
            'Position': 'Finance Officer',
            'Department': 'Finance'
        },
    ]
    return render_template('index.html', title='Home', employees=employees)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        """Creating a new User instance"""
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        flash('Your account has been created! You can now log in.', 'success')
        return redirect('/login')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login method"""
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login was successful')
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)

