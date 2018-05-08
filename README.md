# api-dock

**API Dock**, a web application for managing and testing your APIs.

# INTRODUCTION



# INSTALLATION

**Install `pip` and `virtualenv`**
```
# pip install -U pip
# pip install virtualenv
```

**Clone the application**
```
$ git clone git@github.com:WisdomFusion/api-dock.git
$ cd api-dock/
```

**Create python virtual environment (Linux and macOS shell)**
```
$ virtualenv venv
$ source venv/bin/activate
```

**Create python virtual environment (Windows cmd)**
```
$ python -m venv venv
$ venv\Scripts\activate.bat
$ python -m pip install -U pip
```

**Deploy the application**
```
$ pip install -r requirements.txt
$ mysql -u user -p
> create database apidb;
> \q
$ python run.py db init
$ python run.py migrate
$ python run.py deploy
```

**Add `.env` file to application root folder**
```
APP_CONFIG=development
APP_KEY=
APP_URL=
APP_COVERAGE=1

# PostgreSQL connection
#SQLALCHEMY_DATABASE_URI=postgresql://<db_user>:<password>@<host>[:<port>]/<db_name>
# MySQL connection using PyMySQL
#SQLALCHEMY_DATABASE_URI=mysql+pymysql://<db_user>:<password>@<host>[:<port>]/<db_name>
# MySQL connection using PyMySQL via UNIX sock instead of port
SQLALCHEMY_DATABASE_URI=mysql+pymysql://<db_user>:<password>@<host>/<db_name>?unix_socket=<mysqld_sock_path>
# SQLite connection
#SQLALCHEMY_DATABASE_URI=sqlite:////db/<db_file.sqlite>

CACHE_DRIVER=redis
SESSION_DRIVER=redis

REDIS_HOST=127.0.0.1
REDIS_PASSWORD=null
REDIS_PORT=6379

JWT_SECRET_KEY=123456
JWT_TTL=60

APP_ROOT_ADMIN=sysop

USER_PER_PAGE=20
```
Modify configs above.

**Run the application**
```
$ python run.py runserver
```
