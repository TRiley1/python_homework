from flask import render_template , request , redirect
from app import app 
from models.book_list import books, add_new_book, remove_book
from models.book import Book

@app.route('/books')
def index():
    return render_template('index.html', title = "Tam Riley's Book Store", books = books)

@app.route('/books/<index>')
def single_book(index):
    book = books[int(index)]
    return render_template('book.html', book = book)

@app.route('/books', methods=['POST'])
def add_book():
    bookTitle = request.form['title']
    bookImg = request.form['image']
    bookAuthor = request.form['author']
    bookGenre = request.form['genre']
    bookCheckout = False

    newBook = Book(bookTitle, bookImg, bookAuthor, bookGenre,bookCheckout)
    add_new_book(newBook)
    return redirect("/books")


@app.route('/books/<index>/delete', methods=['POST'])
def removebook(index):
    remove_book(int(index))
    return redirect("/books")







# @app.route('/tasks', methods=['POST'])
# def add_task():
#   taskTitle = request.form['title']
#   taskDesc = request.form['description']
#   newTask = Task(title=taskTitle, description=taskDesc, done=False)
#   add_new_task(newTask)

#   return render_template('index.html', title='Home', tasks=tasks)