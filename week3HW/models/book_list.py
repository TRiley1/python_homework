from models.book import Book 

book1 = Book("Hell's Kitchen","/static/images/gordon.png", "Gordon Ramsay", "Profanity",True)
book2 = Book("1984","/static/images/eye.png", "George Orwell", "non-fiction",False)
book3 = Book("Don Quixote","/static/images/horse.png", "Miguel de Cervantes", "Satire",False)
book4 = Book("The Lord of the Rings","/static/images/wizard.png", "J.R.R Tolkien", "Fantasy",True)
book5 = Book("The Da Vinci Code","/static/images/mona.png", "Dan Brown", "Thriller",False)
book6 = Book("The Da Vinci Code","/static/images/mona.png", "Dan Brown", "Thriller",True)
book7 = Book("Spare","/static/images/spare.png", "Prince Harry", "fiction", False)
book8 = Book("Harry Pooter","/static/images/potter.png", "She who must not be named", "fiction", True)
book9 = Book("The Hobbit","/static/images/hobbit.png", "J.R.R Tolkien", "It Happened", False)

books = [book1,book2,book3,book4,book5,book6,book7,book8,book9]

def add_new_book(book):
    books.append(book)

def remove_book(index):
    books.pop(index)