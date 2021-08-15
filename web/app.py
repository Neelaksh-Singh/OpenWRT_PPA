from flask import Flask ,redirect, request, render_template
from flask_cors import CORS
from multiprocessing import Process
import os
import subprocess

x=subprocess.getoutput("echo ${PWD}" )

app = Flask("ppa")
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# CMD  for getting all the running docker containers
# dc = " docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Ports}}' "

def build(url, deploy_name):
    wrdr=subprocess.getoutput("echo ${PWD}" )

    subprocess.Popen(['./run.sh' ,url , deploy_name], cwd=wrdr)
    
    print("Done with the build")


def get_shell_script_output_using_check_output(url, dp):
    stdout = subprocess.check_output(['./run.sh',url,dp]).decode('utf-8')
    return stdout


@app.route('/')
def mainpage():
    htmlcode = render_template('index.html')
    return htmlcode


@app.route('/test',methods=["GET", "POST"])
def mytest():
    rpLink = request.args.get("repo-url")
    deploy_name = request.args.get("deploy-name")
    print(type(rpLink), type(deploy_name))
    #build(rpLink, deploy_name)
    #return redirect('/')
    #task_cb.start()
    #subprocess.Popen(["./run.sh " ,rpLink , deploy_name])

    if request.method == 'GET':
        task_cb = Process(target=build, args=( rpLink, str(deploy_name)) )
        task_cb.start()
        return redirect('/')
    else:
       return "Build Failed"
