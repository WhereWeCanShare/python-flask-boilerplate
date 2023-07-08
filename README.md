# IMHO Python Flask Boilerplate

[1999] I am new in Python Web Development. Looking for the best practice about the project file/folder structure and could not found any. Only found piece by piece from tutorial.

Thinking it would be worth to have my own Python Flask boilerplate from the ideas and technique in below references.

Also it would be great to share this out to anyone who like it.

## Requirement
This boilerplate is using library list here but feel free to add any to meet your requirement.
- Python 3.7
- dotenv
- flask
- flask-sqlalchmy
- flask-wtf
- gunicorn

*if you plan to use PostgreSQL, this required*
- psycopg2

## Overview structure
`$ tree -a --dirsfirst`
```shell
├── nameyourapp
│   ├── api
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── nameyourmodule
│   │   ├── static
│   │   ├── templates
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   ├── img
│   │   └── js
│   ├── templates
│   │   ├── index.html
│   │   └── layout.html
│   ├── extensions.py
│   ├── forms.py
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── settings.py
├── .env
├── .flaskenv
├── .gitignore
├── Pipfile
├── Pipfile.lock
├── Procfile
├── README.md
└── wsgi.py
```
## How to
- [download](https://github.com/wannadrunk/python-flask-boilerplate/archive/master.zip) this repository
- rename `nameyourapp` according to your project.
- update and develop source code.
- If you use `pipenv`, you can just `$ pipenv install` all basic library will be installed.
- In the development environment, you can run `flask run` to start your app.

## Explanation
- `wsgi.py` will be the entry point for the production environment.
- `.env` where you put all sensitive settings/keys like TOKEN, API-KEY
- `.flaskenv` where put Flask variable e.g. 
```
FLASK_APP=nameyourapp
FLASK_ENV=development
FLASK_DEBUG=true
```
- `nameyourapp/__initi__.py` is the starting point.
- `nameyourapp/models.py` where you define your data tables.
- `nameyourapp/routes.py` your Blueprint module/function
- `nameyourapp/settings.py` put all settings/configurations.
- `api` is the sample Blueprint module.
- `nameyourmodule` put any of your separate module here.

## References and Credits
- [Demystifying Flask’s Application Factory](https://hackersandslackers.com/flask-application-factory/), Hackers & Slacker
- [Organizing Flask Apps with Blueprints](https://hackersandslackers.com/flask-blueprints), Hackers & Slackers
- [Organizing a Flask Project Beyond Single File](https://youtu.be/MbXEQZZSvzk), Pretty Printed YouTube Channel
- [Deploy a Flask App to Heroku With a Postgres Database [2019]](https://youtu.be/FKy21FnjKS0), Pretty Printed YouTube Channel
- [Python Flask Tutorial: Full-Featured Web App Part 11 - Blueprints and Configuration](https://youtu.be/Wfx4YBzg16s), Corey Schafer YouTube Channel
- [Python Flask Tutorial: Full-Featured Web App Part 5 - Package Structure](https://youtu.be/44PvX0Yv368), Corey Schafer YouTube Channel

### Thank you

