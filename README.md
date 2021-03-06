# python-flask [![Build Status](https://travis-ci.com/RichardPoulson/python_flask_example.svg?branch=master)](https://travis-ci.com/RichardPoulson/python_flask_example)
Example Python package that uses the Flask web application framework, based on the [Flask tutorial example](https://github.com/pallets/flask/tree/1.1.2/examples/tutorial).

## Install:
#### Clone the repository:
```
git clone https://github.com/RichardPoulson/python_flask_example
cd python_flask_example
```

#### Create a virtualenv and activate it:
```
python3 -m venv venv
. venv/bin/activate
```

* ###### [Setup virtual environment with PyCharm IDE and Anaconda](https://docs.anaconda.com/anaconda/user-guide/tasks/pycharm/)

#### Install python_example_package in editable mode:
`pip install -e '.[test]'`

#### Run example Flask app:
```
export FLASK_APP=python_flask_example
export FLASK_ENV=development
flask init-db
flask run
```

#### Test
```
pytest
```

#### Run with coverage report::
```
coverage run -m pytest
coverage report
coverage html  # open htmlcov/index.html in a browser
```

## References:
- **[Flask](https://palletsprojects.com/p/flask/ "\"Flask is a lightweight WSGI web application framework.\"")**
- **[Using OAuth 2.0 for Web Server Applications - Google API Client Library for Python](https://github.com/googleapis/google-api-python-client/blob/master/docs/oauth-web.md)**
- PyCharm IDE:
  - [Configure a virtual environment - Help | PyCharm](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html#)
  - [Install, uninstall, and upgrade packages - Help | PyCharm](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html)
- **Testing:**
  - [check-manifest](https://pypi.org/project/check-manifest/)
  - [pytest](https://pypi.org/project/pytest/)
  - [coverage](https://pypi.org/project/coverage/)
- **[Packaging and distributing projects](https://packaging.python.org/guides/distributing-packages-using-setuptools/)**
  - **[The Python Package Index (PyPI)](https://pypi.org/ "\"Find, install and publish Python packages...\"")**
    - [Classifiers](https://pypi.org/search/)
  - [Building and Distributing Packages with Setuptools](https://setuptools.readthedocs.io/en/latest/setuptools.html)
    - [Writing the Setup Script](https://docs.python.org/3.8/distutils/setupscript.html)
    - [Writing the Setup Configuration File](https://docs.python.org/3.8/distutils/configfile.html)
      - [setup() using setup.cfg files - setuptools 46.3.0 documentation](https://setuptools.readthedocs.io/en/latest/setuptools.html#id47)
    - [distutils — Building and installing Python modules](https://docs.python.org/3/library/distutils.html)
- [The Python Standard Library — Python 3.8.3 documentation](https://docs.python.org/3.8/library/index.html)
