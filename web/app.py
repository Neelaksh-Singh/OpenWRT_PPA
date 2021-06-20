from flask import Flask , request, render_template
import func
app = Flask("ppa")

@app.route('/')
def mainpage():
    return func.hello()

@app.route('/test')
def mytest():
    params = {'name': 'User', 'type': 'developer'}
    htmlcode = render_template('index.html', **params)
    return htmlcode