import argparse
import requests
from orm import (
    show_all_books,
    show_all_friends,
    show_all_lendings,
    show_all_lent,
    add_book,
    add_Friend,
    return_book,
    borrow_book
)


def handleDirectData(args):
    # Call the appropriate function based on the parsed arguments
    if args.command == "add_book":
        add_book(args.author, args.title, args.year, args.genre)
    elif args.command == "add_friend":
        add_Friend(args.name, args.surname, args.email)
    elif args.command == "borrow_book":
        borrow_book(args.friend_id, args.title)
    elif args.command == "return_book":
        return_book(args.friend_id, args.title)
    elif args.command == "show_all_books":
        show_all_books()
    elif args.command == "show_all_friends":
        show_all_friends()
    elif args.command == "show_all_lent":
        show_all_lent()
    elif args.command == "show_all_lendings":
        show_all_lendings()


def handleAPIData(args):
    try:
        if args.command == "get_api":
            response = requests.get(url=API_BASE_URL)
            data = response.json()
            print(data)
            return data
        elif args.command == "post_api":
            body = {
                "name": args.name,
                "surname": args.surname,
                "email": args.email
            }
            response = requests.post(f"{API_BASE_URL}", json=body)
            data = response.json()
            print(data)
            return data
        elif args.command == "put_api":
            body = {
                "id": args.id,
                "column": args.column,
                "value": args.value
            }
            response = requests.put(f"{API_BASE_URL}/update", json=body)
            data = response.json()
            print(data)
            return data
        elif args.command == "delete_api":
            response = requests.delete(f"{API_BASE_URL}/delete/{args.id}")
            data = response.json()
            print(data)
            return data
    except Exception as e:
        print(e)


API_BASE_URL = "http://127.0.0.1:5000/friends"


def main():
    # dodanie argumentu, który pokaze czy dostęp
    # jest przez API czy bezpośrednio
    parser = argparse.ArgumentParser(description="Library Management System")

    # subparsery do kolejnych funkcji
    subparsers = parser.add_subparsers(dest="command",
                                       help="Available commands")
    # opcjonalny argument, gdy dodany wysyłamy requesty
    parser.add_argument('--api', action='store_true',
                        help='Use API as data source')

    # api parser

    # get all friends
    subparsers.add_parser("get_api")
    # post new friend
    post_api = subparsers.add_parser('post_api')
    post_api.add_argument("--name", required=True)
    post_api.add_argument("--surname", required=True)
    post_api.add_argument("--email", required=True)

    # update friend
    put_api = subparsers.add_parser('put_api')
    put_api.add_argument("--id", type=int, required=True)
    put_api.add_argument("--column", required=True)
    put_api.add_argument("--value", required=True)

    # delete friend
    delete_api = subparsers.add_parser('delete_api')
    delete_api.add_argument("--id", type=int, required=True)

    # add_book command
    add_book_parser = subparsers.add_parser("add_book")
    add_book_parser.add_argument("--author", required=True)
    add_book_parser.add_argument("--title", required=True)
    add_book_parser.add_argument("--year", type=int, required=True)
    add_book_parser.add_argument("--genre", required=True)

    # add_friend command
    add_friend_parser = subparsers.add_parser("add_friend")
    add_friend_parser.add_argument("--name", required=True)
    add_friend_parser.add_argument("--surname", required=True)
    add_friend_parser.add_argument("--email", required=True)

    # borrow_book command
    borrow_book_parser = subparsers.add_parser("borrow_book")
    borrow_book_parser.add_argument("--friend_id", type=int, required=True)
    borrow_book_parser.add_argument("--title", default="")

    # return_book command
    return_book_parser = subparsers.add_parser("return_book")
    return_book_parser.add_argument("--friend_id", type=int, required=True)
    return_book_parser.add_argument("--title", required=True)

    # show_all_books command
    subparsers.add_parser("show_all_books")

    # show_all_friends command
    subparsers.add_parser("show_all_friends")

    # show_all_lent command
    subparsers.add_parser("show_all_lent")

    # show_all_lendings command
    subparsers.add_parser("show_all_lendings")

    args = parser.parse_args()

    if args.api:
        handleAPIData(args)
    else:
        handleDirectData(args)


if __name__ == "__main__":
    main()

# python3 main.py add_friend --name "Janusz"
# --surname "Bielak" --email "superemail@gmail.com"

# python3 main.py show_all_friends
# python3 main.py add_book --author "Author Name"
# --title "Book Title" --year 2022 --genre "Fiction"

# python3 main.py show_all_books
# python3 main.py add_friend --name "Phili"
# --surname "Smith" --email "mail@gmail.com"

# python3 main.py show_all_friends
# python3 main.py borrow_book --friend_id 1 --title "Book Title"
# python3 main.py show_all_lendings
# python3 main.py show_all_lent
# python3 main.py return_book --friend_id 1 --title "Book Title"

# API COMMUNICATION
# python3 main.py --api get_api

# python3 main.py --api post_api --name 'Tomasz'
#  --surname 'Zan' --email 'dziady@gmail.com'

# python3 main.py --api put_api --id 1 --column
# 'email' --value 'bestmail@gmail.com'

# python3 main.py --api delete_api --id 4
