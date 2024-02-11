import requests
import json
from enum import Enum

class Request(Enum):
    BOOTSTRAP = "bootstrap-static/"
    FIXTURES = "fixtures/"
    PLAYER = "element-summary/"
    GWLIVE = "event/"
    TEAM = "entry/"
    TEAMTRANSFERS = "entry/"
    TEAMPICKS = "team picks"
    CUSTOM = ""

    def __init__(self, argument=None):
        self._argument = argument

    @property
    def argument(self):
        return self._argument

    def path(self):
        if self in [Request.BOOTSTRAP, Request.FIXTURES]:
            return self.value
        elif self == Request.PLAYER:
            if self.argument:
                return self.value + self.argument + "/"
            else:
                return self.value
        elif self == Request.GWLIVE:
            return self.value + self.argument + "/live/"
        elif self == Request.TEAM:
            return self.value + self.argument + "/"
        elif self == Request.TEAMTRANSFERS:
            return self.value + self.argument + "/transfers/"
        elif self == Request.TEAMPICKS:
            return "entry" + self.argument = "event"
        else:
            return ""
class FplService:
    def fetchStatic(self):
        self.fetch(request = Request.BOOTSTRAP)
        self.fetch(request = Request.FIXTURES)

    def fetch(self, request: Request):
        # Make a GET request to the API endpoint
        print("fetching 1")
        path = "https://fantasy.premierleague.com/api/" + request.path()
        response = requests.get(path)
        print("Fetched " + path)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()

            # Store the data in a file (optional)
            with open("../fantasy_premier_league_data.json", "w") as file:
                json.dump(data, file)

            print("Data fetched and stored successfully.")
        else:
            print("Failed to fetch data from the API endpoint.")
