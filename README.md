# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses poetry for Python to create an isolated environment and manage package dependencies. To prepare your system, ensure you have an official distribution of Python version 3.7+ and install Poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py | python -
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/install-poetry.py -UseBasicParsing).Content | python -
```

## Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the Poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Trello Key and Token

to run you need to get a trello key and token. this can be done by signing into trello then getting them from https://trello.com/app-key. you will also need to get the board id of the board you will be using, as well as the list id for youe to do list and done list.

these should be stored in the .env file like so

TRELLO_KEY={your key}
TRELLO_TOKEN={yourtoken}
TRELLO_BOARDID={YourBoardId}
TRELLO_TODOID={To Do list id}
TRELLO_DONEID={Done list id}

## test running
install pytest using following code 
```
pip install -U pytest
```

run this code in external terminal to run tests
```
 poetry run
pytest path/to/test_file
```
## Docker
To build both production and development run
```
$ docker build --target development --tag todo-app:dev .
$ docker build --target production --tag todo-app:prod .
```
and these commands to run it
```
docker run --env-file ./.env -p 5100:80 --mount type=bind,source="$(pwd)"\todo_app,target=/todo_app/app.py todo-app:dev

docker run --env-file ./.env -p 5100:80 --mount type=bind,source="$(pwd)"\todo_app,target=/todo_app/app.py todo-app:prod
```