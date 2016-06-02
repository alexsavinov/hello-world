"""Views module."""

from flask import current_app, render_template, abort, request, url_for, flash, redirect
from jinja2 import TemplateNotFound
from .forms import AddForm
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
from app import engine, Book, books

Session = sessionmaker(bind=engine)
session = Session()

@books.route('/<page>')
def show(page):
    """
    Function to redirect to static pages.
    """

    try:
        return render_template('%s.html' % page)
    except TemplateNotFound:
        abort(404)

@books.route('/')
@books.route('/index')
@books.route('/list')
def list():
    """
    Function to show books list.
    """

    total_rows = session.query(func.count(Book.name)).scalar()
    books = session.query(Book).order_by(Book.id)

    return render_template("list.html",
        title = 'Current list (' + str(total_rows) + ')',
        books = books)

@books.route('/add', methods = ['GET', 'POST'])
def add():
    """
    Function to display page for add item.
    """

    form = AddForm(request.form)
    if request.method == 'GET':
        return render_template('add.html',
            title = 'Adding new book',
            form = form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            book = Book()
            form.populate_obj(book)
            flash('Book "' + book.name + '" added!')
            session.add(book)
            return redirect('/')
        else:
            flash('Adding failed! Fill all fields!')
            return redirect('/add')

@books.route('/edit/<id>', methods = ['GET', 'POST'])
def edit(id):
    """
    Function to display page for edit item.
    """

    book = session.query(Book).get(id)
    form = AddForm(request.form, obj=book)
    if request.method == 'GET':
        return render_template('add.html',
            title = 'Editing book',
            form = form)
    elif request.method == 'POST':
        if form.validate_on_submit():
            book = session.query(Book).get(id)
            form.populate_obj(book)
            flash('Book "' + book.name + '" edited!')
        else:
            flash('Adding failed! Fill all fields!')
        return redirect('/')

@books.route('/delete/<id>')
def delete(id):
    """
    Function to delete item.
    """

    book = session.query(Book).get(id)
    flash('Book "' + book.name + '" deleted!')
    session.delete(book)
    return redirect('/')
