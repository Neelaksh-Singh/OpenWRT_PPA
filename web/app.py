from flask import Flask , request, render_template
from flask_cors import CORS
import func

app = Flask("ppa")
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def mainpage():
    htmlcode = render_template('index.html')
    return htmlcode


@app.route('/test',methods=["GET", "POST"])
def mytest():
    rpLink = request.args.get("repo-url")
    deploy_name = request.args.get("deploy-name")
    func.url_present(rpLink,deploy_name)
    # verName = request.args.get("verName")
    # # if request == 'POST'
    # params = {'rpLink': rpLink, 'imgName': imgName, 'verName': verName}
    
@app.route('/form')
def myform():
    return render_template("form.html")

@app.route('/check',methods=["GET", "POST"])
def check():
    rpLink = request.args.get("repo-url")
    imgName = request.args.get("image-name")
    verName = request.args.get("version")
    return "HELLO"




