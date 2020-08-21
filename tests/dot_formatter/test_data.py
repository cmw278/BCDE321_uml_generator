import os
import json
import gc

_PATH = os.path.dirname(__file__)

_FILE_NAME = '/test-data/dot-formatter.json'
DATA = json.load(open(_PATH + _FILE_NAME))

_FILE_NAME = '/test-data/toybox-toy.json'
TOYBOX_TOY = json.load(open(_PATH + _FILE_NAME))

_FILE_NAME = '/test-data/toybox-toy.gv'
_FILE = open(_PATH + _FILE_NAME)
EXPECTED_OUTPUT = str(_FILE.read())
_FILE.close()

del _PATH
del _FILE_NAME
del _FILE
gc.collect()
