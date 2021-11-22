from flask import render_template
from app import app

@app.route('/' , methods=["GET", "POST"])
def hello_world():
    return render_template('webcardapio.html')