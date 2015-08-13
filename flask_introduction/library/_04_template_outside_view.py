import os

from flask import Flask
from flask import render_template  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Poe"
    return render_template('index.html', library_name=library_name)
