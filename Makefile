# 
init:
	pip install pipenv
	pipenv install --dev
	pipenv run autopep8 -riaa ./src

# commands to run tests go here
test:
	pipenv run pycodestyle ./src