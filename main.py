from flask import Flask
from FPLService.FplService import FplService, Request

app = Flask(__name__)

@app.route("/")
def index():
    print("Start")
    return "Congratulations, it's a web app!"

@app.route("/dataUpdate")
def dataUpdate():
    print("Start")
    service = FplService()
    service.fetchStatic()
    print("END")
    return "Fetching data..."

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
