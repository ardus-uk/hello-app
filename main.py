# main.py

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Congratulation, Peter, it's a web app!"
    
