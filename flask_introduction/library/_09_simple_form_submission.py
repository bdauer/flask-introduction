from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('simple_form.html')
    elif request.method == 'POST':
        return "Submitted title: {}".format(request.form['title'])
