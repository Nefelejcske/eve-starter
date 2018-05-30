# eve-starter

## Installation

- Init virtualenv (optional)  `python -m virtualenv env`
- Activate your virtualenv
  - `env\Script\activate` (Windows)
  - `source env/bin/activate` (Linux)

- Install application
    -  Release: `pip install .`
    -  Development: `pip install -e .[dev]`

## Running tests

Install in development mode then run `pytest`

## Running in development mode via Docker

- `docker-compose build`
- `docker-compose up`

## Sending a request

- `curl http://localhost:5000/`

## TODO

- Add event hooks
- Add flask unit tests
