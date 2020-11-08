APP_NAME=web_app

attach_web:
	docker-compose exec $(APP_NAME) /bin/zsh

attach_bot:
	docker-compose exec bot_app /bin/zsh

start_docker:
	docker-compose up -d

stop_docker:
	docker-compose stop

clean_docker:
	/bin/zsh clean_docker.sh

app_restart:
	docker-compose stop $(APP_NAME)
	docker-compose up -d $(APP_NAME)

app_logs:
	docker-compose logs -f web_app

all_logs:
	docker-compose logs -f --tail="100"

down_docker:
	docker-compose down

rebuild_docker:
	docker-compose up --force-recreate --build -d

force_rebuild_docker: down_docker rebuild_docker

build:
	docker-compose -f docker-compose-build.yml build

push:
	docker login
	docker-compose -f docker-compose-build.yml push

build_push: build push
