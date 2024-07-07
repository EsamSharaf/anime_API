![This is an alt text.](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.postimg.cc%2Fxqr8Nmtn%2Fflask.png&f=1&nofb=1&ipt=9515c2d647d468e886dcf2bd9226d268e9c37a77778dfeef39cb5982a5fdf754&ipo=images "This is a sample image.")
# Anime API Project

## Description
Flask REST API for Anime Database. SQLAlchemy is implemented to interact with PostgreSQL.

The project deployed on Render.com as service with additional service for the database.

## Environment

### Create and activate the environment

```
python -m venv venv

venv source venv/bin/activate
```

### Install dependecies

```
pip install -r requirements.txt
```

## Load Data into Database

```
export FLASK_DEBUG=1
```

```
python import_data_into_db.py
```

## Development

### Export environment variables

```
export FLASK_DEBUG=1
```

```
export FLASK_APP=/home/esharaf/projects/anime_API/autoapp.py
```


### Run Flask

```
flask run
```

## Running Tests

```
pytest
```