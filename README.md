#### Introduction 

Basic linting and type checking configuration for Python application.


### Installation

This command will run the setup from setup.py and install all dependencies.

```sh
pip install .
```

### Run linter

This command will run all pylint on all .py files in your project. 
Note that pylint takes the configuration from .pylintrc but we can more the configuration to setup.cfg
https://pylint.readthedocs.io/en/latest/tutorial.html

```sh
pylint ./
```

you can alos check specific files
```sh
pylint app.py
```

### Run type checking

This command will run type chekcing on your .py files
!! Mypy will not check unannotated python functions and variables. Make sure to annotate your code.
I recommend getting familir with Dynamic vs Static typing in Python as well as using Protocol
https://peps.python.org/pep-0544/

```sh
mypy .
```