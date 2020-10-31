# コンテナ実行
start_docker:
	sudo /etc/init.d/docker start

docker_exec := docker exec -it
con := mocrat_main
login_container:
	${docker_exec} ${con} /bin/bash

up_mocrat:
	docker-compose up

build_mocrat:
	docker-compose up --build

down_docker_compose:
	docker-compose down


# mocrat
rc :=
compose_exec := docker-compose exec 
exec_mocrat_app := docker container exec mocrat-app

# mocrat_app
container_name := mocrat-app
login_mocrat:
	${compose_exec} ${container_name} bash
	
run_django_manage:
	${compose_exec}${container_name}  python3 manage.py ${rc}

pipinstall_requirements:
	${compose_exec} ${container_name} pip install --upgrade -r requirements.txt

makemigrations:
	${compose_exec} ${container_name} python3 manage.py makemigrations
	${compose_exec} ${container_name} python3 manage.py makemigrations mocrat_user

migrate:
	${compose_exec} ${container_name} python3 manage.py migrate

# mocrat_db
login_mocrat_db:
	make login_mocrat container_name=mocrat_db

# discord_app
login_discord_app:
	make login_mocrat container_name=discord_app
	
# mocrat_utils
# TODO: なんでexecじゃないとrequests通らないん？？runだと新規でコンテナ立てるから？
# automation_utils
asakatsu_scheduler:
	${exec_mocrat_app} sh -c "python3 -c 'from utils.automation_utils import chibamoku_scheduler; chibamoku_scheduler.asakatsu_scheduler()'"

asakatsu_closer:
	${exec_mocrat_app} sh -c "python3 -c 'from utils.automation_utils import chibamoku_scheduler; chibamoku_scheduler.asakatsu_closer()'"

furikaeri_reminder:
	${exec_mocrat_app} sh -c "python3 -c 'from utils.automation_utils import chibamoku_scheduler; chibamoku_scheduler.furikaeri_reminder()'"

discord_heartbeat:
	${exec_mocrat_app} sh -c "python3 -c 'from utils.automation_utils import chibamoku_scheduler; chibamoku_scheduler.discord_heartbeat()'"

# twitter_utils
twitter_auth_userid := chiba_moku2
twitter_post := Hello！
call_twitter_post_util:
	${exec_mocrat_app} python3 -c "from utils.twitter_utils import twitter_requests_utils; twitter_requests_utils.call_twitter_post('${twitter_auth_userid}', '${twitter_post}')"

auto_fav_word := 駆け出しエンジニア
auto_fav_count := 10
call_auto_fav_by_query:
	${exec_mocrat_app} python3 -c "from utils.twitter_utils import twitter_requests_utils; twitter_requests_utils.call_auto_fav_by_query('${twitter_auth_userid}', '${auto_fav_word}', ${auto_fav_count})"

# custom command
username=admin
email=sample@testmail.org
passwd=Passw0rd
create_custom_superuser: ## This is create super user for 1line, need name,email,passwd(default=admin,sample@testmail.org,Passw0rd)
	${exec_mocrat_app} python3 ./manage.py custom_create_superuser --username ${username} --email ${email} --password ${passwd}

# mocrat_db
PGPASSWORD :=
PGUSER :=
PGHOST :=
PGPORT :=
PGDATABASE :=

attach_db:
	${run_mocrat_app} psql -h  -p 5433 -U postgres -W postgres test_db
	
clear_database:
	${run_mocrat_app} sh -c "sleep 1 && PGPASSWORD=${PGPASSWORD} psql -U ${PGUSER} -h ${PGHOST} -p ${PGPORT} -c 'drop database ${PGDATABASE};' && PGPASSWORD=${PGPASSWORD} psql -U ${PGUSER} -h ${PGHOST} -p ${PGPORT} -c 'create database ${PGDATABASE};'"

delete_all_db_and_migrations:
	sudo rm -rf mocrat_db/data/
	sudo rm -rf mocrat_app/*/migrations/

clone_db_volume:
	sudo cp -r mocrat_db/data/ mocrat_db/data_buckup

# 環境
chown_user:
	sudo chown -R ubuntu:ubuntu .

# Git
day := `date +"%Y_%m_%d"`
m := autopush ${day}
branch := origin master
autopush: ## This is auto push module, need commit message(default=autopush)
	make chown_user
	git add .
	git commit -m "${m}"
	git push ${branch}

pull:
	git pull ${branch}

force_pull:
	git fetch ${branch}
	git reset --hard origin/master

clear-gitcache:
	git rm -r --cached .
	
u := 
p :=
add_netrc:
	touch ~/.netrc
	echo "machine github.com" > ~/.netrc
	echo "login ${u}" >> ~/.netrc
	echo "password ${p}" >> ~/.netrc

mail :=
add_github_config:
	git config --global user.name ${u}
	git config --global user.email ${mail}