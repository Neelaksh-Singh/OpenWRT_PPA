from flask import Flask , request, render_template
import func
app = Flask("ppa")

@app.route('/')
def mainpage():
    return func.hello()

@app.route('/test' ,methods=["GET"])
def mytest():
    rpLink = request.args.get("rpLink")
    imgName = request.args.get("imgName")
    verName = request.args.get("verName")
    # if request == 'POST'
    params = {'rpLink': rpLink, 'imgName': imgName, 'verName': verName}
    htmlcode = render_template('index.html', **params)
    return htmlcode
@app.route('/form')
def myform():
    return render_template("form.html")
