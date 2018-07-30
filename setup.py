"""Setup for boilerplate flask backend."""
from setuptools import setup, find_packages

meta = {}
exec(open('./vf_boilerplate/version.py').read(), meta)

setup(
    name='vf_boilerplate',
    version=meta['__version__'],

    description='',
    long_description='',

    packages=find_packages(),

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
