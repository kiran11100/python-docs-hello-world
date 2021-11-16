from flask import Flask
import hashlib
app = Flask(__name__)

@app.route("/")
def hello():
    surname="anumala"
    result=hashlib.sha256(surname.encode())
    return "Hello,".result
