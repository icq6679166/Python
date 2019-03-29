from flask import Flask

app = Flask(__name__)


@app.route('/')
def fool():
    return "Hello flask, from python"


app.run(port=5550, host='0.0.0.0', debug=True)
