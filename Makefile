# コンテナ実行
docker_exec := docker exec -it
container := discord_app
login_container:
	${docker_exec} ${container} /bin/bash

up_mocrat:
	docker-compose up

build_mocrat:
	docker-compose up --build


# mocrat_app
rc :=
run_mocrat_app := docker-compose run mocrat_app
login_mocrat_app:
	${run_mocrat_app} bash
	
run_django_manage:
	${run_mocrat_app} python3 manage.py ${rc}

pipinstall_requirements:
	${run_mocrat_app} pip install --upgrade -r requirements.txt

makemigrations:
	${run_mocrat_app} python3 manage.py makemigrations
	${run_mocrat_app} python3 manage.py makemigrations mocrat_user

migrate:
	${run_mocrat_app} python3 manage.py migrate

username=admin
email=sample@testmail.org
passwd=Passw0rd
create_custom_superuser: ## This is create super user for 1line, need name,email,passwd(default=admin,sample@testmail.org,Passw0rd)
	${run_mocrat_app} python3 ./manage.py custom_create_superuser --username ${username} --email ${email} --password ${passwd}

# mocrat_db
PGPASSWORD :=
PGUSER :=
PGHOST :=
PGPORT :=
PGDATABASE :=

attach_db:
	${run_mocrat_app} psql -h  -p 5433 -U postgres -W postgres test_db
	
clean_database:
	${run_mocrat_app} sh -c "sleep 1 && PGPASSWORD=${PGPASSWORD} psql -U ${PGUSER} -h ${PGHOST} -p ${PGPORT} -c 'drop database ${PGDATABASE};' && PGPASSWORD=${PGPASSWORD} psql -U ${PGUSER} -h ${PGHOST} -p ${PGPORT} -c 'create database ${PGDATABASE};'"

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