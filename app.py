from flask import Flask

app = Flask(__name__)

visitors = 0

@app.get("/")
def index():
    global visitors
    visitors += 1
    return f"<h1>Hallo, verden!</h1> <p>Du er besøkende nummer {visitors}.</p>"