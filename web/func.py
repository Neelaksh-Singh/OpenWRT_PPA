import os
import subprocess

# CMD for getting all the running docker containers
dc = " docker ps --format 'table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Ports}}' "

def build(url, deploy_name):
    subprocess.Popen(["./run.sh " ,"url" , "deploy_name"] )
    print("Done with the build")

def container():
    return subprocess.getoutput(dc)

#def myfiles():
#    return subprocess.getoutput("../my-test/x")
