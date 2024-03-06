## flask app routing
from flask import Flask


##create simple flask application
app=Flask(__name__)

@app.route("/",methods=["GET"])
def welcome():
    return "welcom to the devendra github"

@app.route("/index",methods=["GET"])
def indexpage():
    return "welcom to the index page"




if __name__=="__main__":
    app.run(debug=True)