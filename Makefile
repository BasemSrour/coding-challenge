upbuild: build up

up:
	docker-compose -f local.yml up

build:
	docker-compose -f local.yml build

run:
	docker-compose -f local.yml run $(filter-out $@,$(MAKECMDGOALS))

restart:
	docker-compose -f local.yml restart $(filter-out $@,$(MAKECMDGOALS))

shell:
	docker-compose -f local.yml exec django /entrypoint.sh ./manage.py shell_plus

bash:
	docker-compose -f local.yml exec django /entrypoint.sh bash

down:
	docker-compose -f local.yml down $(filter-out $@,$(MAKECMDGOALS))

destroy:
	docker-compose -f local.yml down -v

createsuperuser:
	docker-compose -f local.yml exec django /entrypoint.sh ./manage.py createsuperuser

makemigrations:
	docker-compose -f local.yml run --rm django ./manage.py makemigrations $(filter-out $@,$(MAKECMDGOALS))

migrate:
	docker-compose -f local.yml run --rm django ./manage.py migrate $(filter-out $@,$(MAKECMDGOALS))

urls:
	docker-compose -f local.yml run django python manage.py show_urls

logs:
	docker-compose -f local.yml logs -f $(filter-out $@,$(MAKECMDGOALS))

test:
	docker-compose -f local.yml run --service-ports --rm django ./manage.py test $(filter-out $@,$(MAKECMDGOALS))

debug:
	docker-compose -f local.yml run --service-ports --rm $(filter-out $@,$(MAKECMDGOALS))

rm_pyc:
	find . -name '__pycache__' -name '*.pyc' | xargs rm -rf


test_local:
	docker-compose -f local.yml exec django /entrypoint.sh ./manage.py test --settings=config.settings.test $(filter-out $@,$(MAKECMDGOALS))

stagingup:
	docker-compose -f staging.yml up -d --build

load_db:
	docker-compose -f local.yml stop django celeryworker celerybeat
	docker cp backup-2021-03-05.sql.gz $(shell docker ps -qf "name=postgres"| head -n 1):/backups
	docker-compose -f local.yml exec postgres restore backup-2021-03-05.sql.gz
	docker-compose -f local.yml up -d
