# 
init:
	pip install pipenv
	pipenv install --dev

# commands to run tests go here
test:
	pipenv run pycodestyle ./src