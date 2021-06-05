from flask import render_template, url_for, redirect, request, flash
from flask_login import login_user,logout_user, login_required, current_user
from . import auth
from ..models import User
from .forms import login_Form, registration_Form
from .. import db

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = login_Form()
    if form.validate_on_submit:
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember.data)
            next = request.args.get('next')
            return redirect(next or url_for('main.index'))
    return render_template('auth/login.html', form=form)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = registration_Form()
    if form.validate_on_submit():
        user = User(email=form.email.data, username=form.username.data, password=form.password.data)
        db.create_all()
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
