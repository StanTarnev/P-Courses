# Intro to Flask

**Duration: 60 minutes**

## Learning Objectives

- Be able to use pip to install packages
- Understand how to set up lightweight server with Flask
- Set up a basic Flask project.

## Introduction

If you're developing a web app in Python, chances are you will be using a framework.

A framework "is a code library that makes a developer's life easier when building reliable, scalable, and maintainable web applications" by providing reusable code or extensions for common operations. There are a number of frameworks for Python, including Flask, Tornado, Pyramid, and Django.

Exactly what is implemented in the framework and what is left for the developer to write varies from framework to framework. In this course we will be using  Flask and Django. The biggest difference between Flask and Django is:

- Flask implements a bare-minimum and leaves the bells and whistles to add-ons or to the developer

- Flask is also easy to get started with as a beginner because there is little boilerplate code for getting a simple app up and running.

- Django follows a "batteries included" philosophy and gives you a lot more out of the box.


We will start today by looking at Flask and then adding an ORM to deal with Database access later.

### The brief

We're going to make a simple To-Do web application.

### Initial setup

In order to get our application up and running, there are a few steps to follow.

```bash
# terminal

mkdir todo_list
cd todo_list

python -m venv .env
source .env/bin/activate
```

Now that you have a virtual environment created and activated, you can finally install Flask in it:

### Pip

Now that we're working within our virtual environment, we can start to use the power of pip! Pip is a package manager that allows us to use all sorts of external packages in our apps. It is analagous to NPM for JavaScript, or Gems for Ruby.

We want to be using pip for python 3 so we will use the command `pip3` to install our dependancies.

Since we're going to make a simple web server, we're going to use [Flask](http://flask.pocoo.org/), a microframework that is similar to Ruby's Sinatra, or JavaScript's Express.

The first thing we'll do is download Flask:

```bash
# terminal

pip3 install Flask
```

Now that we have Flask set up, let's set up a simple base structure for our app and make sure that we can connect to the server.

### Hello World!

Let's create a package called app, that will host the application. Make sure you are in the todo_list directory and then run the following command:

```bash
# terminal

mkdir app
```

Next we will create the `__init__.py` file to store our package configuration and open our project in Atom.

```bash
# terminal

touch app/__init__.py

atom .
```

In `__init__.py` we will add the following code

```python
# __init__.py

from flask import Flask

app = Flask(__name__)

from app import routes
```

> It may be confusing that there are two separate references to app. The app package is defined by the app directory and is referenced in the `from app import routes` statement.

>The app variable is used as an instance of Flask, which makes it a member of the app package.

The code above simply creates the application object as an instance of class Flask imported from the flask package.

The `__name__` variable passed to the Flask class is a Python predefined variable, which is set to the name of the module in which it is used.

Flask uses the location of the module passed here as a starting point when it needs to load associated resources such as template files.

Passing `__name__` is almost always going to configure Flask in the correct way.

The application then imports the routes module, which doesn't exist yet.

### Routes

So what goes in the routes module?

Routes are the different URLs that the application implements. In Flask, handlers for the routes are written as Python functions, called view functions.

View functions are mapped to one or more URLs so that Flask knows what logic to execute when a client requests a given URL

We will start off creating our `routes.py` file in the app package and adding a new function for a home route.

```bash
touch app/routes.py
```
In `routes.py `we will import our Flask instance from the app package.

We will then add a new route to `/` and below write the function that will execute when we go to that route in the browser.

```python
# routes.py

from app import app

@app.route('/')
def index():
    return "Hello, World!"
```

This view function will just return a greeting as a string.

The `@app.route` line above the function is a decorator. In this case, the `@app.route` decorator creates an association between the URL and the function.

In this example the decorator associates the URL `/` to this function. This means that when a web browser requests this URL, Flask is going to execute this function and pass the return value of it back to the browser as a response. If this does not make complete sense yet, it will in a little bit when you run this application.

### Running the application

To run the application, we need to have a Python script at the top-level that defines the Flask application instance.

Let's call this script todo_list.py, and define it as a single line that imports the application instance:

```bash
# terminal

touch todo_list.py
```

```python
# todo_list.py

from app import app
```

Believe it or not, the application is now complete!

Before running it, though, Flask needs to be told how to import it, by setting the FLASK_APP environment variable:

```bash
export FLASK_APP=todo_list.py
```

Are you ready to be blown away? You can run your first web application, with the following command:

```bash
# terminal

flask run
```
You should see the following:

```bash
* Serving Flask app "todo_list.py"
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

So now if we go to our browsers and visit `http://localhost:5000` we should see Hello World! in the browser window!

### Route parameters

We may also want to pass in some parameters from our url.

For, example we may take in a name and return a string of "Hello " plus the name

To do this we need to declare these path variables in our route using `<>` arrows with the name of our variable inside.

We then pass that variable to the function.  

Let's create a new route.

```python
# routes.py

from app import app

@app.route('/<name>')
def index(name):
    return f"Hello {name}!"
```
> Note we have to stop and start the server mfor this change to take effect.

Now if we go to  http://127.0.0.1:5000/Ally we should see this string printed out!


### Setting up the environment variable.

One more thing.... Since environment variables aren't remembered across terminal sessions, you may find it a bit tedious to always have to set the FLASK_APP environment variable when you open a new terminal window.

Flask allows you to register environment variables that you want to be automatically imported when you run the flask command.

To use this option you have to install the `python-dotenv` package:

```bash
# terminal

pip3 install python-dotenv
```

Then you can just write the environment variable name and value in a .flaskenv file in the top-level directory of the project:

```bash
# terminal

touch .flaskenv
```

```python
# .flaskenv

FLASK_APP=todo_list.py
```

Doing this is optional. If you prefer to set the environment variable manually, that is perfectly fine, as long as you always remember to do it.

One final thing we can do is sort out a pesky business of having to restart the server every time we make a change.

In the `routes.py` file, change 'Hello World' to 'Python is awesome!'.

If we refresh the browser nothing happens. We have to restart the server in terminal. Go to terminal and press `ctr+c`, then run the `flask run` command again. Refresh the browser and our change should now show.

To fix this we can use Flasks development environment which will allow hot reloading.

In the same `.flaskenv` file we will add another environment variable.

```python
# .flaskenv
FLASK_APP=todo_list.py
FLASK_ENV=development # ADDED
```

Now if we make a change to the routes file our app should update on a browser refresh.

Try it out!

Next we will look at Templates to get our to-do list displaying!

## Summary

Flask is a simple, lightweight server that allows us to quickly set up web applications and gives us the tools to create routes and run flask instances from the terminal.
