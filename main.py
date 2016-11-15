import json
import urllib.request
from pprint import pprint

import mbta_helper
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)


app.config['DEBUG'] = True


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if name:
        name = name.upper()
    return render_template('hello.html', name=name)


@app.route('/mbta_helper/', methods=['GET', 'POST'])
def helper():
    if request.method == 'POST':
        address = str(request.form['place_name'])
        result = mbta_helper.print_stop(address)
        mbta = result[0]
        distance =result[1]
        if result != None:
            return render_template('mbta_response.html', mbta = mbta, distance = distance, place_name = address)
        else:
            return render_template('bad_response.html')
    return render_template('mbta_form.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
