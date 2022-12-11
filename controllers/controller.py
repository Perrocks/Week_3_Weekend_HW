from flask import render_template, request, redirect
from app import app
from models.books import *
from models.book import *

@app.route('/books')
def index():
    return render_template('index.html', title='Library Home', books_html=books)

@app.route('/books/<index>')
def book(index):
    page_title = f"Book: {books[int(index)].title}"
    return render_template('book_info.html', title=page_title, books_html=books[int(index)])


@app.route('/books', methods=['POST'])
def add_book():
  title = request.form['book_title']
  author = request.form['author']
  genre = request.form['genre']
  description = request.form['description']
  availability = True if 'availability' in request.form else False
  new_book = Book(title=title, author=author, genre=genre, description=description, availability=availability)
  add_new_book(new_book)
  return redirect('/books')

@app.route('/books/delete/<index>', methods=['POST'])
def delete(index):
  delete_book(int(index))
  return redirect('/books')