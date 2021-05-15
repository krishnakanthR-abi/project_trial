
from flask import Flask, request
import database

app = Flask(__name__)

@app.route('/')
def fun():
    return("...SERVER...")

@app.route('/login', methods=['POST'])
def login():
    print(request.form)
    login_data = request.form.to_dict()
    print("Name",login_data['name'])
    print("Number",login_data['number'])
    print(database.add_user(login_data['name'],login_data['number']))
    return "logged in"

if __name__ == '__main__':
    app.run(debug=True, port=9000)