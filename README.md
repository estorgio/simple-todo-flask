# Simple TODO

A simple TODO app made with Flask.

## Live demo

- [https://simple-todo-dot-estorgio-demo.uw.r.appspot.com](https://simple-todo-dot-estorgio-demo.uw.r.appspot.com/)
- [https://simple-todo-flask.onrender.com](https://simple-todo-flask.onrender.com/)

## Running the app

### Local

```bash
# Create virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install dependencies
$ pip3 install -r requirements.txt

# Run database migration
$ flask db upgrade

# Configure settings
$ cp .env-example .env
$ nano .env

# Launch app
$ flask run
```

### Google App Engine (GAE)

```bash
# Configure App Engine settings
$ cp app.yaml-example app.yaml
$ nano app.yaml

# Deploy to GAE
$ gcloud app init
$ gcloud app create
$ gcloud app deploy

# Open in browser
$ gcloud app browse -s simple-todo
```
