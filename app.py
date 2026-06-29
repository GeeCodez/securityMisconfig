from flask import Flask, render_template
import os
from dotenv import load_dotenv
load_dotenv()


app=Flask(__name__)

app.config["DEBUG"]=False
app.config["SECRET_KEY"]=os.getenv("SECRET_KEY")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/crash")
def crash():
    return 1/0

if __name__=="__main__":
    app.run()