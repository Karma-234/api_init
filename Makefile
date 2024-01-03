env:
	python3 -m venv env
run-env:
	source env/bin/activate
mgs:
	python manage.py makemigrations
mg:
	python manage.py migrate