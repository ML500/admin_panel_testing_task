# admin_panel_testing_task

## Used in the project:
* Django
* DRF
* Vue Js v3
* Sqlite3
* Djoser
* pytest


## Installation
* Clone a project from GitHub
  * git clone https://github.com/ML500/admin_panel_testing_task
* Create and activate virtual environment
  * cd admin_panel
  * python3 -m virtualenv -p python3 venv
  * source venv/bin/activate
* Install dependecies
  * pip install -r requirements.txt
* Make Data Base Migrations
  * python manage.py makemigrations
  * python manage.py migrate
* Load dump
  * python manage.py loaddata fixtures/auth.json
* Run backend
  * python manage.py runserver
* Install or update vue
  * cd ..
  * cd frontend
  * sudo npm install -g @vue/cli
* Install axios
  * npm install axios
* Run frontend
  * npm run serve

## Superuser:
 * login: admin
 * password: admin

## Run pytest:
 * cd admin_panel/backend
 * pytest
