
#Jasper Cheung
#SoftDev1 pd7
#HW #06: Echo Echo Echo
#2017-10-2

from flask import Flask, render_template, request 

app = Flask(__name__)

@app.route("/")
def home():
    print "\n\n\n"
    print "***DIAG: this Flask obj***"
    print app
    print "***DIAG: request.obj***"
    print request
    print "***DIAG: request.args***"
    print request.args
    return render_template('template.html')

@app.route("/echo")
def welcome():
    return render_template('echo.html', name = request.args['u_name'], method = request.method)

if (__name__ == "__main__"):
    app.debug = True
    app.run()
