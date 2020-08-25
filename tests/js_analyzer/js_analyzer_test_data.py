import esprima
import json
import os
import gc

path = os.path.dirname(__file__)

# Toybox class file
file_name = '/test-data/ToyboxToy/Toybox.js'
file_ = open(path + file_name)

# esprima is an external library so is assumed to be tested already
RAW_DATA = esprima.parse(file_.read())
file_.close()

TOYBOX_CLASS = RAW_DATA.body[0]

ADDTOY_METHOD = TOYBOX_CLASS.body.body[1]
NEWNAME_IDENTIFIER = ADDTOY_METHOD.value.params[0]

# expected dict representation of addToy()
file_name = '/test-data/add-toy.json'
file_ = open(path + file_name)

ADDTOY_DICT = json.load(file_)

# expected dict representation of Toybox
file_name = '/test-data/Toybox.json'
file_ = open(path + file_name)

TOYBOX_DICT = json.load(file_)

del file_
del path
del file_name
gc.collect()
