from flask import Flask, jsonify

app = Flask(__name__)

# Define your users
users = [
    {"id": 1, "name": "John Doe", "email": "john.doe@example.com"},
    {"id": 2, "name": "Jane Smith", "email": "jane.smith@example.com"},
    {"id": 3, "name": "Bob Johnson", "email": "bob.johnson@example.com"},
]

# Define a route that returns the list of users
@app.route('/users')
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
