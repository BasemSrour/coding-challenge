upbuild: build up

up:
	docker-compose -f local.yml up

build:
	docker-compose -f local.yml build

run:
	docker-compose -f local.yml run $(filter-out $@,$(MAKECMDGOALS))

shell:
	docker-compose -f local.yml run --rm django python manage.py shell_plus

bash:
	docker-compose -f local.yml run --rm django bash

createsuperuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

makemigrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate

urls:
	docker-compose -f local.yml run django python manage.py show_urls

test:
	docker-compose -f local.yml run --rm django pytest
