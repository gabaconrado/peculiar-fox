# Peculiar Fox

[![CircleCI](https://circleci.com/gh/gabaconrado/peculiar-fox/tree/master.svg?style=svg)](https://circleci.com/gh/gabaconrado/peculiar-fox/tree/master)

> Minimal marketlist app, designed for testing/personal purposes

## Getting started

The simplest way to get the system up-and-running is using pip and django locally (more options on
[docker](#Docker))

### Prerequisites

You need to have [Python 3](https://www.python.org/downloads/).

To run the system through docker it is required to have [Docker](https://docs.docker.com/ee/) and
[Docker Compose](https://docs.docker.com/compose/install/).

**Note:** During the development the versions used were 70.0.1(firefox) and 0.26.0(geckodriver)

### Installing

To install the dependencies create a virtual environment(optional) and install the modules:

```bash
python -venv venv   # (Optional)
pip install -r etc/base/requirements.txt
```

Then, go to the source directory and run the application using the django manager:

```bash
cd src
python manage.py migrate --no-input     # Generate database
python manage.py runserver 0.0.0.0:8000
```

The application will be available at `http://localhost:8000`

### Testing

To run the test it is required to install the _development requirements file_:

```bash
pip install -r etc/development/requirements.txt
```

#### Unit/Functional

The tests are located in the _src/tests_ directoy and are divided into **unit** and **functional**

Also, to run the functional tests in the host machine, it is required to have
[Firefox](https://www.mozilla.org/pt-BR/firefox/new/) and
[Geckodriver](https://github.com/mozilla/geckodriver/releases).

```bash
cd src
pytest .
```

#### Codestyle

To run the linter:

```bash
cd src
flake8 .
```

### Deployment

To deploy the system it is necessary to install the _deploy requirements file_:

```
pip install -r etc/deploy/requirements.txt
```

There are some _environment variables_ that must be set in order to run succesfully:

|Name|Value|Description|
|----|-----|-----------|
|DEBUG|0|Set the Debug to zero to prevent information leaking to the user|
|SECRET_KEY|<random>|Secret key used by Django|
|DJANGO_ALLOWED_HOSTS|CQDN/IP|List of hostnames that can run the app sepparated by single spaces|

Collect the static files in order to provide them and run the server using [Guinicorn](https://gunicorn.org/):

```bash
cd src
python manage.py collectstatic --no-input
python manage.py migrate --no-input     # Generate database
gunicorn peculiar_fox.wsgi:application --bind 0.0.0.0:8000
```

The application will be available at `http://localhost:8000`

## Docker

There is also pre-configured _docker-compose_ files to run the system in an development and
deployment requirement.

The base files is in _/etc/base_, the directories _/etc/development_ and _/etc/deploy_ contains
the necessary files to run each specific environment.

**Note:** The deployment environment depends on environment variables, nginx configuration file and
a certificate/private key to be available in host. For more information on Nginx click [here](http://nginx.org/en/docs/).
To generate a self-signed test certificate click [here](https://www.ibm.com/support/knowledgecenter/en/SSMNED_5.0.0/com.ibm.apic.cmc.doc/task_apionprem_gernerate_self_signed_openSSL.html).

### Development (Docker)

The port mapping for the docker development container is listed below:

|Port|Description|
|----|-----------|
|8000|Where the django service will be running|
|3000|Available for debugging (usign [PTVSD](https://pypi.org/project/ptvsd/) for instance)

To run the system, invoke **docker-compose** passing the wanted files:

```bash
cd etc/base     # This is important
docker-compose -f docker-compose.yml -f ../development/docker-compose.yml up --build -d
```

The application will be available at `http://localhost:8000`

### Deploy (Docker)

The port mapping for the docker deploy container is listed below:

|Port|Description|
|----|-----------|
|80|Where the nginx proxy will be listening for http|
|443|Where the nginx proxy will be listening for https|

The deploy environment need to have a certificate and a private key file in _etc/deploy/nginx_ called
_servercert.pem_ and _serverkey.pem_. Also it is required to define a environment variable called
**SERVER_URL** with the server's CQDN/IP.

To run the system, invoke **docker-compose** passing the wanted files:

```bash
cd etc/base     # This is important
docker-compose -f docker-compose.yml -f ../deploy/docker-compose.yml up --build -d
```

The application will be available at `https://<SERVER_URL>`

## Built With

- [Django](https://www.djangoproject.com/)

## Versioning

The versioning is made with [SemVer](https://semver.org/)
