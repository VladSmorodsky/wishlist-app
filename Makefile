port ?= '9000'

makemigrations:
	docker compose exec -it api python manage.py makemigrations

migrate:
	docker compose exec -it api python manage.py migrate

runserver:
	docker compose exec -it api python manage.py runserver 0.0.0.0:$(port)

shell:
	docker compose exec -it api python manage.py shell