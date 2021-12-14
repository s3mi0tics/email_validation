from flask import Flask

# from flask_bcrypt import Bcrypt

app = Flask(__name__)

app.secret_key = "2a836880-e4cc-4953-9cfd-2392f0a03b1b"

# bcrypt = Bcrypt(app)