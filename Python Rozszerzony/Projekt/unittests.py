import unittest
from main import handleDirectData, handleAPIData
from orm import session, borrow_book
from models import Book, Friend, Lending, LendingStates
from argparse import Namespace


class TestDirectFunctions(unittest.TestCase):

    def test_add_book_command(self):
        # Namespace is a container for arguments
        test_args = Namespace(command="add_book", author="John Doe",
                              title="Sample Book", year=2022, genre="Fiction")

        # Call the function
        handleDirectData(test_args)

        # Query the database to check if the book was added
        added_book = session.query(Book).filter_by(author="John Doe",
                                                   title="Sample Book").first()

        # Assert that the book exists in the database
        self.assertIsNotNone(added_book)
        self.assertEqual(added_book.author, "John Doe")
        self.assertEqual(added_book.title, "Sample Book")
        self.assertEqual(added_book.year, 2022)
        self.assertEqual(added_book.genre, "Fiction")

    # non existing borrow
    def test_borrow_book_command(self):
        test_args = Namespace(command="borrow_book", friend_id=1,
                              title='non existing title')

        # Use assertRaises to check for the expected exception
        with self.assertRaises(Exception) as context:
            handleDirectData(test_args)

        # Check if the exception message matches the expected message
        self.assertEqual(str(context.exception),
                         "Book unavailable!")

    def test_borrow_book_existing_command(self):
        # korzystamy tylko z istniejących w bibliotece metod,
        # tylko co do nich mamy pewność że są poprawne
        session.add(Book(author='Tolkien',
                         title='Lord of the Rings',
                         year=1970, genre='fantasy'))
        session.add(Friend(name='Tom', surname='Sawyer',
                           email='email@gmsil.com'))
        session.commit()

        test_args = Namespace(command="borrow_book",
                              friend_id=1,
                              title='Lord of the Rings')
        # wywołanie funkcji
        handleDirectData(test_args)

        # czy coś zostało dodane do lendings
        lendings = session.query(Lending).all()
        self.assertIsNotNone(lendings)

        # czy friend też był dobrze obsłużony
        friend = session.query(Friend).filter(Friend.id == 1).first()
        self.assertEqual(friend.lending[0].id, 1)

    def test_return_book_command(self):
        # Add a lending to simulate a borrowed book
        session.add(Book(author='Tolkien',
                         title='Lord of the Rings',
                         year=1970, genre='fantasy'))
        session.add(Friend(name='Tom',
                           surname='Sawyer',
                           email='email@gmail.com'))

        # jak dzoszliśmy aż tutaj w testach to borrow działa
        borrow_book(1, 'Lord of the Rings')
        session.commit()

        test_args = Namespace(command="return_book",
                              friend_id=1,
                              title='Lord of the Rings')

        # Call the function
        handleDirectData(test_args)

        # Check if lending has been updated
        # jedyny dodany element to nowy lending
        updated_lending = session.query(Lending).first()
        self.assertIsNotNone(updated_lending)
        self.assertIsNotNone(updated_lending.return_date)

        # Check if book state has been updated
        updated_book = session.query(Book).filter(Book.id == 1).first()
        self.assertEqual(updated_book.lend_state, LendingStates.ON_SHELF)

    def test_return_book_friend_unavailable(self):
        session.add(Friend(name='Tom', surname='Sawyer',
                           email='email@gmail.com'))
        session.commit()
        test_args = Namespace(command="return_book",
                              friend_id=999,
                              title='Some Book Title')

        # Use assertRaises to check for the expected exception
        with self.assertRaises(ValueError) as context:
            handleDirectData(test_args)

        # Check if the exception message matches the expected message
        self.assertEqual(str(context.exception), "Friend unavailable!")

    def test_return_book_books_unavailable(self):
        session.add(Book(author='Tolkien',
                         title='Lord of the Rings',
                         year=1970,
                         genre='fantasy'))
        session.commit()
        test_args = Namespace(command="return_book",
                              friend_id=1,
                              title='Non-existing Book Title')

        # Use assertRaises to check for the expected exception
        with self.assertRaises(ValueError) as context:
            handleDirectData(test_args)

        # Check if the exception message matches the expected message
        self.assertEqual(str(context.exception), "Books unavailable!")


class TestApiCalls(unittest.TestCase):

    def test_get_api(self):
        # clear the session
        session.query(Friend).delete()
        session.add(Friend(name='Tom',
                           surname='Something',
                           email='email@gmail.com'))
        session.commit()

        test_args = Namespace(command="get_api")

        data = handleAPIData(test_args)
        # comapare result
        self.assertEqual(data,
                         [{'email': 'email@gmail.com', 'id': 1,
                           'name': 'Tom', 'surname': 'Something'}])

    def test_post_api(self):
        # clear the session
        session.query(Friend).delete()
        # session.add(Friend(name='Tom',
        #                    surname='Something',
        #                    email='email@gmail.com'))
        session.commit()

        test_args = Namespace(command="post_api",
                              name='Angela',
                              surname='Rollings',
                              email='rollngs@gmail.com')

        data = handleAPIData(test_args)
        # compare server response
        self.assertEqual(data, {'message': 'Friend added successfully'})

        # check if friend was actually added
        friends = session.query(Friend).all()
        self.assertEqual(len(friends), 1)

    def test_delete_non_existing_api(self):
        # session.query(Friend).delete()  # clear the session
        session.add(Friend(name='Tom',
                           surname='Something',
                           email='email@gmail.com'))
        session.commit()

        # print(session.query(Friend).first().id)
        test_args = Namespace(command="delete_api", id=1000)

        data = handleAPIData(test_args)
        # compare server response
        self.assertEqual(data, {'error': 'Unable to delete'})


if __name__ == '__main__':
    unittest.main()
