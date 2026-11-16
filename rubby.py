#import flask
from flask import Flask

#creates a flask application object
app = Flask(__name__)

#create static endpoints
@app.route("/")
#this function handles requests for /home
def home():
    return "Welcome"

print(a)


#flask starts the local web server
app.run()




