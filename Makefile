.PHONY: all server server-typecheck server-install-packages \
	server-create-database \
	client client-install-packages client-build \
	docker


all: server client

docker:
	git archive --format tar --output verbum-client.zip master

server:
	@$(MAKE) server-install-packages server-typecheck server-create-database

client: client-install-packages client-build

client-install-packages:
	(cd client && npm install)

client-build:
	(cd client && npm run build)

server-typecheck:
	mypy --ignore-missing-imports src

server-install-packages:
	(cd src && pipenv install)

server-create-database:
	rm -fr data/*.sqlite3
	pipenv run python scripts/db_setup.py


