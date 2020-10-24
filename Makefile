










# コンテナ実行
up_mocrat:
	docker-compose up

rc :=
run_mocrat_app := docker-compose run mocrat_app

# mocrat_app
login_mocrat_app:
	${run_mocrat_app} bash
	
run_django_manage:
	${run_mocrat_app} python3 manage.py ${rc}

pipinstall_requirements:
	${run_mocrat_app} pip install --upgrade -r requirements.txt

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