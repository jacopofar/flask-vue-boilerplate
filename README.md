Nothing to see here, go away




## How to build and deploy somewhere

TODO

## How to prepare Docker image

TODO

## How to run in dev mode

Create the local virtualenv:

    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt

Start the server in dev mode, it will listen on port 8080:

    uwsgi uwsgi.development.ini

Then on a new shell run the frontend service:

    yarn run serve

It will expose a server on port 8090, and proxy all requests starting with `/app` or `/login` to the backend running at port 8080.
__NOTE__: the `/login` endpoint in dev mode is a *fake* login service which always emits a token, only for testing.

Now every change to the code will trigger a restart. The frontend is capable of a precise hot reload, while the backend simply restarts on changes.

If you change uWSGI or Vue configurations you still need a real restart.