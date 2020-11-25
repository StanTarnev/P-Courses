# Setting up your environment

**Duration: 30 minutes**

## Learning Objectives

- Be able to set up a virtual environment
- Be able to use pip to install packages
- Be able to import modules / packages as needed

## Introduction

If we want to keep our project and its dependencies self-contained, Python provides a number of ways of doing this. In fact, in the past, it has been quite a contentious issue at times, with many different ways of accomplishing - essentially - the same thing.

Some of the tools you'll see mentioned include:

- virtualenv
- pyenv
- pyenv-virtualenv
- virtualenvwrapper
- pyenv-virtualenvwrapper
- pipenv
- venv
- pyvenv

We're going to be looking at `venv` today. It comes included with Python3, and has a straightforward, easy to use syntax.

### Starting Out

We're going to make a very, very basic web server. Firstly, let's create a directory for our project.

```bash
mkdir my_site
cd my_site
```

Next up, we're going to create a _virtual environment_. This ensures that all of our app's dependencies are stored within this directory - not globally. We could also, for example, use a different version of Python for this app if we wanted to.

```bash
python3 -m venv .env
```

Here, we're running `python3`, and asking it to execute a particular module, venv (`-m venv`). Finally, we're telling Python to store all of its project-specific information in a folder called `.env`, which it will create for us.

We can check this by running `ls -a` - we should see a `.env` directory now.

We've set up our virtual environment, but we also need to _activate_ it. We can do this with the following command:

```bash
source .env/bin/activate
```

You will see the command prompt changing - it should now begin `(.env)`. This tells you that you're working within your virtual environment.

Should you wish to exit the virtual environment, you can run:

```bash 
deactivate
```

### Pip

Now that we're working within our virtual environment, we can start to use the power of pip! Pip is a package manager that allows us to use all sorts of external packages in our apps. It is analagous to NPM for JavaScript, or Gems for Ruby.

Since we're going to make a simple web server, we're going to use [Flask](http://flask.pocoo.org/), a microframework that is similar to Ruby's Sinatra, or JavaScript's Express.

The first thing we'll do is download Flask:

```bash
pip install Flask
```

Next, we'll create our app file:

```bash
touch app.py
```

If we open up our app.py file, we can create our web server!

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

Finally, we can run our app with the following command:

```bash
FLASK_APP=app.py flask run
```

Go to [http://localhost:5000](http://localhost:5000) and you should see your app.

### Importing modules and packages

In the above example, we're import Flask to help us to write a web app.

We're going to play with this idea a bit more, but first, we need to define what modules and packages are.

A **module** in Python is simply a file with a .py extension. It might contain classes, functions, and variables that we can import into our program.

**Packages** in Python are namespaces that can themselves contain multiple packages, or modules. Each package (directory) **must** contain a special file named `__init__.py` to indicate that it is a Python package.

Let's create a **package** called `helpers`, and a module called `calculator.py`.

```bash
mkdir helpers
touch helpers/__init__.py
touch helpers/calculator.py
```

Let's fill out our calculator, using functions for add, subtract, multiply, and divide.

```python
def add(a, b):
    return a+b
    
def subtract(a, b):
    return a-b
    
def divide(a, b):
    return a/b
    
def multiply(a, b):
    return a*b
```

Finally, let's import our calculator into app.py. We can do this in two ways:

```
from helpers import calculator
```

Or:

```
import helpers.calculator
```

This brings in _all_ of the things that are defined in the calculator module.

It's very important to note that we're using a lower-case 'c' for 'calculator' here. That's because we are importing the module, and the filename starts with a small 'c'.

Finally, let's use the functions from our calculator module in our app, defining a route which takes in two parameters to add.

```python
@app.route("/add/<a>/<b>")
def add(a, b):
    a = int(a)
    b = int(b)
    return str(calculator.add(a, b))
```

We can go to [http://localhost:5000/add/10/5](http://localhost:5000/add/10/5) to check our work.

### Importing specific things from modules

We could have instead chosen just to import the `add` function from our module. To do so, we could have done something like this:

```python
from helpers.calculator import add
```

We would then need to change the name of our route, as we have two functions named `add` in scope.

```python
@app.route("/add/<a>/<b>")
def add_route(a, b):
    a = int(a)
    b = int(b)
    return str(add(a,b))
```

Notice that we also call the function by using the name we imported.