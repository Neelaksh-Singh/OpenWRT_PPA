from flask import Flask , request, render_template
import func
app = Flask("ppa")

@app.route('/')
def mainpage():
    return "<pre>"+ func.container() + "</pre>"

@app.route('/test',methods=["GET", "POST"])
def mytest():
    rpLink = request.args.get("repo-url")
    imgName = request.args.get("image-name")
    func.url_present(rpLink,imgName)
    # verName = request.args.get("verName")
    # # if request == 'POST'
    # params = {'rpLink': rpLink, 'imgName': imgName, 'verName': verName}
    htmlcode = render_template('index.html', input=func.container())
    return htmlcode
@app.route('/form')
def myform():
    return render_template("form.html")

@app.route('/check',methods=["GET", "POST"])
def check():
    rpLink = request.args.get("repo-url")
    imgName = request.args.get("image-name")
    verName = request.args.get("version")
    return "HELLO"




