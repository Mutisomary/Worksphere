from flask import render_template, flash, redirect
from app import app, db
from app.forms import LoginForm, RegistrationForm, EmployeeForm
from app.models import User, Employee


@app.route('/')
@app.route('/index')
def index():
    employees = Employee.query.all()
    return render_template('index.html', employees=employees)

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

@app.route('/add_employee', methods=['GET', 'POST'])
def add_employee():
    form = EmployeeForm()
    if form.validate_on_submit():
        new_employee = Employee(
            name=form.name.data,
            contact_information=form.contact_information.data,
            position=form.position.data,
            department=form.department.data
        )
        db.session.add(new_employee)
        db.session.commit()
        return redirect('/index')    
    return render_template('add_employee.html', form=form)
