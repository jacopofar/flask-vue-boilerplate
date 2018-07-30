Nothing to see here, go away




## How to build and deploy somewhere

TODO

## How to prepare Docker image

TODO

## How to run in dev mode

To run the backend component you can be brave and try Pipenv:

    make run-dev-with-pipenv

it should create a virtualenv, install the packages and run the server from there.

Otherwise create the local virtualenv:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

 and start the server in dev mode, it will listen on port 8080:

    uwsgi uwsgi.development.ini

Run the frontend service (no matter how the backend was started):

    yarn install
    yarn run serve

It will expose a server on port 8090, and proxy all requests starting with `/app` or `/login` to the backend running at port 8080.

__NOTE__: the `/login` endpoint in dev mode is a *fake* login service which always emits a token, only for testing.

Now every change to the code will trigger a restart. The frontend is capable of a precise hot reload, while the backend simply restarts on changes.

If you change uWSGI or Vue configurations you still need a real restart.

## Test

TODO: backend tests...

    yarn run test:unit

## Linting

The project includes linting for Python and JS:

For the backend, using pipenv:

    make lint-with-pipenv

or after activating the virtualenv:

    make lint

For JS:

    yarn run lint