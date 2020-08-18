import os
import json

_PATH = os.path.dirname(__file__)
_JSON_FILE = '/test-data/dot-formatter.json'

DATA = json.load(open(_PATH + _JSON_FILE))

_JSON_TOYBOX_TOY = '/test-data/toybox-toy.json'

TOYBOX_TOY = json.load(open(_PATH + _JSON_TOYBOX_TOY))
