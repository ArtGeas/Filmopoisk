# Filmopoisk
On this site you can see information about the films. If you register on the site, the user can add movies to favorites in his personal account

## Requirements

* Python 3.10.6

* Node 19.8.1
  
* Flask==2.1.3

## Build

```shell
pip install -r requirements.txt

pip install -r requirements.dev.txt
```

1. Create models (clean up DB and create models from import)
```shell
python create_tables.py
```

2. Download data to DB
```shell
python load_fixture.py
```

### Bash (Linux/MACOS)
```shell
export FLASK_APP=run.py
export FLASK_ENV='development'
flask run
```

### CMD (Windows)
```shell
set FLASK_APP=run.py
set FLASK_ENV=development
flask run
```

### PowerShell (Windows)
```shell
$env:FLASK_APP = "run"
$env:FLASK_ENV = "development"
flask run
```

## Tests
```shell
pytest .
```
