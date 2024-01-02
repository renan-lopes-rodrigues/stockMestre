start:
	docker-compose up --build --force-recreate

stop:
	docker-compose down

db_migrate:
	alembic revision --autogenerate