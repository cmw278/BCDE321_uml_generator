import os
import json

_PATH = os.path.dirname(__file__)
_JSON_FILE = '/test-data.json'

DATA = json.load(open(_PATH + _JSON_FILE))
