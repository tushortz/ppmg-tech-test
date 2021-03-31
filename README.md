# PPMG Tech Test

Test provided by PPMG

## requirements
* python v >= 3.5

## How to run
* create a virtual environment using the following command

```sh
$ python -m venv env
```

Activate the virtual environment using

```sh
$ env/Scripts/activate # windows
$ source env/bin/activate # other os platforms
```

> **Note**: creating the virtual environment step above is optional.

## Running the application

```sh
$ python manage.py migrate
$ python manage.py runserver
```