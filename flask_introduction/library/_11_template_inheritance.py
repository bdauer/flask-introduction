from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def hello_world():
    if request.method == 'GET':
        return render_template('form_with_template_inheritance.html')
    elif request.method == 'POST':
        # Insert
        return "Submitted title: {}".format(request.form['title'])
