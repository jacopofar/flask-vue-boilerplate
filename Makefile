lint:
	python3 -m flake8 --exclude='.venv,node_modules'

run-dev:
	$(eval REQUIREMENTS_HASH := $(shell shasum requirements.txt|cut -d " " -f1))
	python3 -m venv /tmp/venv_$(REQUIREMENTS_HASH)
	/tmp/venv_$(REQUIREMENTS_HASH)/bin/pip3 install -r requirements.txt
	/tmp/venv_$(REQUIREMENTS_HASH)/bin/uwsgi uwsgi.development.ini

run-dev-with-pipenv:
	# pipenv runs on windows, but uwsgi requires this argument :(
	pipenv install --python 3
	$(eval PIPENV_VENV_PATH := $(shell pipenv --venv))
	pipenv run uwsgi -H $(PIPENV_VENV_PATH) uwsgi.development.ini

lint-with-pipenv:
	pipenv run python3 -m flake8 --exclude='.venv,node_modules'