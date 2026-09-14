build:
	./build.sh

render-start:
	gunicorn portfolio.wsgi

install:
	poetry install

collectstatic:
	poetry run python manage.py collectstatic --noinput

migrate:
	poetry run python manage.py migrate

start:
	poetry run python manage.py runserver
test:
	poetry run python manage.py test portfolio.task_manager
test-cov:
	poetry run coverage run manage.py test
	poetry run coverage xml