from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from models import Book,Lending,Friend,Base



# db_url = "mysql+mysqlconnector://root:@localhost:4001/python"
db_url = 'sqlite:///library.db'

engine = create_engine(db_url)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


def add_book(author, title, year, genre):
    book = Book(author=author, title=title, year=year, genre=genre)
    session.add(book)
    session.commit()

# friend table
def add_Friend(name, surname, email):
    friend = Friend(name=name, surname=surname, email=email)
    session.add(friend)
    session.commit()

def delete_Friend(id):
    to_delete_friend = session.query(Friend).filter(Friend.id == id).first()
    if to_delete_friend:
        session.delete(to_delete_friend)
        session.commit()
    else:
        raise ValueError("Incorrect ID")
    
def show_all_friends():
    friends = session.query(Friend).all()
    for f in friends:
        print(f"ID: {f.id}, name: {f.name}, surname: {f.surname}, email: {f.email}")
    return friends
    

def update_Friend(id, field, value):
    to_update_friend = session.query(Friend).filter(Friend.id == id).first()
    if to_update_friend:
        # czy obiekt ma taki atrybut
        if hasattr(to_update_friend, field):
            # update
            setattr(to_update_friend, field, value)
            session.commit()
        else:
            raise ValueError(f"Field '{field}' does not exist in the Friend model")
    else:
        raise ValueError("Incorrect ID")




def get_Friend_byId(id):
    friend = session.query(Friend).filter(Friend.id == id).first()
    if friend:
        return friend
    else:
        raise ValueError("Not correct id!")

    
    


def borrow_book(friend_id, title=''):
    # znajdź możliwą do wypożyczenia książkę z danym tytułem
    book = session.query(Book).filter(Book.title == title, Book.lend_state == 'on_shelf').first()
    friend = session.query(Friend).filter(Friend.id == friend_id).first()
    if book:
        new_lending = Lending(friend_id=friend_id, lend_date=datetime.now(), book_id=book.id)
        session.add(new_lending)
        friend.lending.append(new_lending)  # dodanie wypożyczenia do książki
        book.lend_state = 'lent'
        session.commit()
        return
    raise ValueError("Book unavailable!")


def return_book(friend_id, title):
    # pobieramy wszystkie książki o danym tytule i wypożyczone
    books_ids = [book.id for book in session.query(Book).filter(Book.title == title, Book.lend_state == 'lent').all()]
    friend = session.query(Friend).filter(Friend.id == friend_id).first()

    for lending in friend.lending:
        # szukamy wypożyczenia zrobionego przez znajomego, aktualizujemy je
        if lending.book_id in books_ids:
            lending.return_date = datetime.now()
            # zmieniamy też stan książki, 'on_shelf' i dodajemy jeszcze wypożyczenie do jej stanu
            book = session.query(Book).filter(Book.id == lending.book_id).first()
            book.lend_state = 'on_shelf'
            book.lendings.append(lending)
            session.commit()


def show_all_books(books=session.query(Book).all()):
    for book in books:
        print(f"ID: {book.id}, title: {book.title}, lend_state: {book.lend_state}, authors: {book.author}")






# pokazujemy wszystkie teraz wypożyczone
def show_all_lent():
    books = session.query(Book).filter(Book.lend_state == 'lent').all()
    show_all_books(books)


# pokazujemy wszystkie wypożyczenia
def show_all_lendings():
    lendings = session.query(Lending).all()
    for l in lendings:
        print(
            f"ID: {l.id} friend name: {l.friend.name}, lend_date: {l.lend_date}, return_date: {l.return_date}, book_id: {l.book_id}")

