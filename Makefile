serve:
	FLASK_APP=./api.py FLASK_ENV=production pipenv run flask run

lint:
	pipenv run pylint src tests *.py

test:
	pipenv run pytest