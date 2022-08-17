from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)


@app.get("/")
def home():
    return "Hello World"



if __name__ == '__main__':
    app.run(debug=True)
