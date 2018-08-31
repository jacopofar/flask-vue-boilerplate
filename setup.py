"""Setup for boilerplate flask backend."""
from setuptools import setup, find_packages

meta = {}
exec(open('./vf_boilerplate/version.py').read(), meta)

setup(
    name='vf_boilerplate',
    version=meta['__version__'],

    description='Flask, uWSGI and Vue.js boilerplate and example app',
    long_description='''Boilerplate to show a Flask + Vue.js modern-ish app.
It includes linting, automated test, live/hot reload, optional pipenv support,
Docker build, CI/CD and whatnot.''',

    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[
        'pytest',
        'pytest-cov',
        'flask',
        'uwsgi',
        'Flask-Dance',
        'flake8',
        'pydocstyle'
    ]
)
