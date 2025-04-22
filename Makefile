port ?= '9000'

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

runserver:
	python manage.py runserver 0.0.0.0:$(port)

shell:
	python manage.py shell