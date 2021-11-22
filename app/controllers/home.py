from app import app

@app.route('/' , methods=["GET", "POST"])
def hello_world():
    return "<p>Hello, World!</p>"