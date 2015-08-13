from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('form_with_static.html')
    elif request.method == 'POST':
        return "Submitted title: {}".format(request.form['title'])
