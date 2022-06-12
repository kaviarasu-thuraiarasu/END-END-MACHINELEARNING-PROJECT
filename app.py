from flask import Flask
from crypt import method

app = Flask(__name__)


@app.route('/',method=method.GET)
def index():
    return "application started"

if __name__ =="__main__":
 app.run(debug=True)