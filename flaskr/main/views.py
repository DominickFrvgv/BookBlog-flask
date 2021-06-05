from flask import render_template, redirect, url_for
from ..models import User, Book
from . import main
from .forms import edit_Form, book_Form
from flask_login import login_required, current_user
from .. import db

@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    form = book_Form()
    if form.validate_on_submit():
        post = Book(title=form.title.data, author=form.author.data, rating=form.rating.data, user_id=current_user.id)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('.index'))
    posts = Book.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', form=form, posts=posts)

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)

@main.route('/edit-about-me', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = edit_Form()
    if form.validate_on_submit():
        current_user.about_me = form.about.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        return redirect(url_for('.index', username=current_user.username))
    form.about_me = current_user.about_me
    return render_template('edit-about-me.html', form=form)
