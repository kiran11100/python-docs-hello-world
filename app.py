from flask import Flask
import hashlib
app = Flask(__name__)
app.debug=False
@app.route("/")
def hello():
    surname = "anumala"
    result = hashlib.sha256(surname.encode('utf-8')).hexdigest()
    data = "Hello   " + result
    return data
