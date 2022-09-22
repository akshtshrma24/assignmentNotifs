import requests
import json
from constants import * 

# gets the Classes as a JSON


def getRawClasses():
    response = requests.get(
        URL,
        params=PARAMS_GET_DATA,
        headers=HEADERS_GET_DATA)
    return json.loads(response.text)
