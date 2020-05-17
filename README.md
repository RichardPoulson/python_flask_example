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

###### Or on Windows cmd:
```
py -3 -m venv venv
venv\Scripts\activate.bat
```

###### [Or with PyCharm IDE](https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html# "\"PyCharm makes it possible to use the virtualenv tool to create a project-specific isolated virtual environment.\"")

#### Install python_example_package:
`pip install -e .`

#### Run example Flask app:
```
export FLASK_APP=python_flask_example
export FLASK_ENV=development
flask init-db
flask run
```
##### Or on Windows cmd:
```
set FLASK_APP=python_flask_example
set FLASK_ENV=development
flask init-db
flask run
```

#### Test
```
pip install '.[test]'
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
