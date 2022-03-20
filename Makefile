serve:
	FLASK_APP=./api.py FLASK_ENV=production pipenv run flask run

check:
	pipenv run pylint src tests *.py
	pipenv run pytest

lint:
	pipenv run pylint src tests *.py

test:
	pipenv run pytest

