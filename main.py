from flask import Flask
from FPLService.FplService import FplService, Request
import jinja2

app = Flask(__name__)

@app.route("/")
def index():
    print("Start")
    environment = jinja2.Environment()
    template = environment.from_string("Hello, {{ name }}!")
    template.render(name="RENDERED")
    return template.render(name="Return Value")  #"Congratulations, it's a web app!"

@app.route("/dataUpdate")
def dataUpdate():
    print("Start")
    service = FplService()
    service.fetchStatic()
    print("END")
    return "Fetching data..."

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
