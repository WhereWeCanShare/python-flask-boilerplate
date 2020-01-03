# IMHO Python Flask Boilerplate

[1999] I am new in Python Web Development. Looking for the best practice about the project file/folder structure and could not found any. Only found piece by piece from tutorial.

Thinking it would be worth to have my own Python Flask boilerplate from the ideas and technique in those reference.

Also it would be great to share this out to anyone who like it.

## Requirement
This boilerplate is using library list here but feel free to add any to meet your requirement.
```shell
python3 -m venv venv
source venv/bin/activate
pip install dotenv
pip install flask
pip install flask-sqlalchemy
pip install gunicorn

## if you plan to use PostgreSQL, this required
pip install psycopg2

```

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


## References and Credits
- [Demystifying Flask’s Application Factory](https://hackersandslackers.com/flask-application-factory/), Hackers & Slacker
- [Organizing Flask Apps with Blueprints](https://hackersandslackers.com/flask-blueprints), Hackers & Slackers
- [Organizing a Flask Project Beyond Single File](https://youtu.be/MbXEQZZSvzk), Pretty Printed YouTube Channel
- [Deploy a Flask App to Heroku With a Postgres Database [2019]](https://youtu.be/FKy21FnjKS0), Pretty Printed YouTube Channel
- [Python Flask Tutorial: Full-Featured Web App Part 11 - Blueprints and Configuration](https://youtu.be/Wfx4YBzg16s), Corey Schafer YouTube Channel
- [Python Flask Tutorial: Full-Featured Web App Part 5 - Package Structure](https://youtu.be/44PvX0Yv368), Corey Schafer YouTube Channel

### Thank you
![cHoo logo](https://chookiat.com/biz/wp-content/uploads/2017/04/logo-choo300x96.png)

> If you found this boilerplate is useful and would like to buy me a coffee, here is the link https://paypal.me/ChookiatJ
