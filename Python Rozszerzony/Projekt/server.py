from flask import Flask, jsonify, request
from orm import add_Friend, show_all_friends, delete_Friend, update_Friend, get_Friend_byId

app = Flask(__name__)


# CRUD - Create Read Update Delete

# ustawienie nazwy serwera
# app.config['SERVER_NAME'] = 'localhost:3000'
#
# app.run(debug=True, host='0.0.0.0')

@app.route("/")
def main():
    return "<p>Kurs programowania w Pythonie</p>"


@app.route("/friends", methods=['GET'])
def get_all_friends():
    friends = show_all_friends()
    friends_list = [
        {"id": friend.id, "name": friend.name, "surname": friend.surname, "email": friend.email}
        for friend in friends
    ]
    return jsonify(friends_list)


@app.route("/friends", methods=['POST'])
def add_friend():
    data = request.json

    name = data.get('name')
    surname = data.get('surname')
    email = data.get('email')

    # funkcja z ORM
    add_Friend(name, surname, email)

    # zwrócenie odpowiedzi
    return jsonify({'message': 'Friend added successfully'})


@app.route("/friends/delete/<int:id>", methods=['DELETE'])
def delete_friend(id):
    try:
        delete_Friend(id)
        return jsonify({'message': 'Friend deleted successfully'})
    except:
        return jsonify({'error': 'Unable to Delete'}), 500


@app.route("/friends/update", methods=['PUT'])
def update_friend():
    data = request.json
    id = data.get('id')
    column = data.get('column')
    value = data.get('value')
    try:
        update_Friend(id, column, value)
        friend = get_Friend_byId(id)
        friend_json = {"name": friend.name, "surname": friend.surname, "email": friend.email}
        return jsonify(friend_json)
    except:
        return jsonify({'error': 'Unable to Update'})




if __name__ == "__main__":
    app.run(debug=True)
