server:
	python3 manage.py runserver

reqs:
	pip install -r requirements/requirements.txt

makemigrations:
	python3 manage.py makemigrations

migrate:
	python3 manage.py migrate