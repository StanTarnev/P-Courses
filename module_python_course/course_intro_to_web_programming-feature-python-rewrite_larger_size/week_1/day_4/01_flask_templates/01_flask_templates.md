# Flask Templates

**Duration: 100 minutes**

## Learning Objectives

- Understand how to set up templates with Flask
- Understand how Flasks architecture relates to MVC
- Create Views in Flask

## Introduction

Now that we have Flask set up we will continue working on the same application, and in particular, generate more elaborate web pages that have a complex structure and many dynamic components.

To do this we are going to use Templates.

> Download and open the start point. start the app and go to http://localhost:5000

We have a start point for a simple ToDo list. There are 2 files in the model folder. A Task class which stores a title, description and a boolean value to signify if the task is complete or not.

We also have a todo_list script that gives us some dummy data and function to add a new task (more on that later!)

We are going to code up our route to view all of the tasks and have them rendered using an HTML template.

### Adding some HTML

So far the view function in the application returns a simple Hello World string. What we __could__ do now is expand that returned string into a complete HTML page, maybe something like this:

> No need to code along with this as it is just an example that instructor will show.

```python
# controller.py

from app import app

@app.route('/')
def index():
    return '''
<html>
    <head>
        <title>Home Page - My To-Do List</title>
    </head>
    <body>
        <h1>My Todo List!</h1>
    </body>
</html>'''
```

So now if we restart the server and go to our browser we would see our header in the window.

The solution used above to deliver HTML to the browser is not good.

Consider how complex the code in this view function will become when we have the To-Do List tasks from users, which are going to constantly change. The application is also going to have more view functions that are going to be associated with other URLs, so imagine if one day I decide to change the layout of this application, and have to update the HTML in every view function. This is clearly not an option that will scale as the application grows.

If you could keep the logic of your application separate from the layout or presentation of your web pages, then things would be much better organised, don't you think?

Templates help achieve this separation between presentation and business logic.

### Templates

In Flask, templates are written as separate files, stored in a templates folder that is inside the application package. So, after making sure that you are in the root directory, create the directory  in the app package to store the templates:

> Code along from this point, stopping server (ctrl+c) if it is running

```bash
mkdir app/templates
```

And in here let's create a new template for the index page.

```bash
touch app/templates/index.html
```

Now we will add some HTML code in this template.

```html
<!-- index.html -->

<html>
    <head>
        <title>{{ title }} - My To-Do List</title>
    </head>
    <body>
        <h1>My Todo List!</h1>
    </body>
</html>
```

This is mostly a standard HTML page. The interesting thing in this page is that there are a couple of placeholders for the dynamic content, enclosed in {{ ... }} sections. These placeholders represent the parts of the page that are variable and will only be known at runtime.

Now the view function can be simplified.

To use this template we will need to import a function from Flask called `render_template`.

This function takes a template filename and a variable list of template arguments and returns the same template, but with all the placeholders in it replaced with actual values.

```python
# controller.py

from flask import render_template # ADDED
from app import app

@app.route('/')
def index():
    return render_template('index.html', title='Home') # MODIFIED
```

> The render_template() function implements the Jinja2 template engine that comes with Flask. Jinja2 substitutes {{ ... }} blocks with the values of the arguments provided in the render_template() call.

Now if we start the server and go to http://localhost:5000 we should see the header.

### More Dynamic Content

The logged in user will probably want to see their list in the home page, so we will extend the application to support that.

We will use some fake objects to get some To-Do List items to display:

If you look in the models folder we have a Task class and a todo list script. The Todo List populates a list with a couple of tasks and has some methods to return the list and to add a new task (more on that later!). Normally we wouldn't have a class like this but because we aren't using databases or any other source this will suffice to cover the concepts.

In the view we will get the list of tasks. We will then pass the tasks to the template. To get the tasks we will import them from the todo_list module. We will then pass them to our template.

```python
# controller.py

from flask import render_template
from app import app
from app.models.todo_list import tasks # ADDED

@app.route('/')
def index():
    return render_template('index.html', title='Home', tasks=tasks) # MODIFIED
```

On the template side we have to solve a new problem. The list of tasks can have any number of entries, it is up to the view function to decide how many tasks are going to be presented in the page. The template cannot make any assumptions about how many tasks there are, so it needs to be prepared to render as many tasks as the view sends.

For this type of problem, `Jinja2` offers a `for loop` control structure.

### Loops

You have seen how Jinja2 replaces placeholders with actual values during rendering, but this is just one of many powerful operations Jinja2 supports in template files.

For example, templates also support control statements, such as if statements and for loops.

These are coded inside blocks.

```html
<!-- index.html -->

<html>
    <head>
        <title>{{ title }} - My To-Do List</title>
    </head>
    <body>
        <h1>My Todo List!</h1>
        {% for task in tasks %}  <!-- ADDED -->
        <div>
          <p>
            {{ task.title }}: <b>{{ task.description }}</b>
          </p>
        </div>
        {% endfor %}
    </body>
</html>
```

So now that we have passed the list of tasks to the template we can access it and loop over each task to display a new div for each one. This will work regardless of how many tasks are passed through.

## Conditional Rendering

With our tasks we may want to show if the task has been completed.

We can achieve this with conditionals. We will display a green tick (using UTF-8 code) if the tasks completed value is True

```html
<!-- index.html -->

<html>
    <head>
        <title>{{ title }} - My To-Do List</title>
    </head>
    <body>
        <h1>My Todo List!</h1>
        {% for task in tasks %}
        <div>
          <p>
            {{ task.title }}: <b>{{ task.description }}</b>
            {% if task.done %}  <!-- ADDED -->
            <span> &#9989;</span>
            {% endif %}
          </p>
        </div>
        {% endfor %}
    </body>
</html>
```

## Template Inheritance

Most web applications these days have a navigation bar at the top of the page with a few frequently used links, such as a link to edit your profile, to login, logout, etc.

We __could__ add a navigation bar to the index.html template with some more HTML, but what happens if we add more pages to the site and want the same nav bar in each. We don't really want to have several copies of the navigation bar in many HTML templates, it is a good practice to not repeat yourself if that is possible.

`Jinja2` has a template inheritance feature that specifically addresses this problem. This allows us to move the parts of the view that are common to all templates to a base template, from which all other templates extend.

Let's create a new template called `base.html` in the templates folder.

```bash
touch app/templates/base.html
```

And we will move the common view code into this template. this will also have our Navigation. For now we will just have a link to the home page.

To define where the view from our templates will go we use another Jinja2 construct called a block.

Blocks are given a unique name, which templates can reference when they provide their content.

We will call this block `content`.

```html
<!--base.html -->

<html>
    <head>
      <title>{{ title }} - My To-Do List</title>
    </head>
    <body>
        <ul>
          <li><a href="/">Home</a></li>
        </ul>
        <hr>
        {% block content %}

        {% endblock %}
    </body>
</html>
```

Now we can simplify index.html by making it inherit from `base.html`:

```html
<!-- index.html -->

{% extends "base.html" %}

{% block content %}
    <h1>My Todo List!</h1>
    {% for task in tasks %}
    <div>
      <p>
        {{ task.title }}: <b>{{ task.description }}</b>
        {% if task.done %}
        <span> &#9989;</span>
        {% endif %}
    </p>
    </div>
    {% endfor %}
{% endblock %}
```

Our `index.html` now only has the main content of this specific page.

The extends statement establishes the inheritance link between the two templates, so that Jinja2 knows that when it is asked to render index.html it needs to embed it inside base.html.

The two templates have matching block statements with name content, and this is how Jinja2 knows how to combine the two templates into one.

So if we create additional pages for the application, we can create them as templates that inherit from the same `base.html` template, and all the pages of the application share the same look and feel without duplication.

### Adding a new task

We can also add a new task to our list using a form. Again, as we aren't using databases these won't persist if we stop the server but will show the concept of getting data from a form.

Let's start by adding a form to the top of our list. This form will make a POST request to a route we will code up later.

```html
<!-- index.html -->

{% extends "base.html" %}

{% block content %}
    <h1>My Todo List!</h1>

    <form action="/add-task" method="post"> <!-- ADDED -->
      <label for="title">Title</label>
      <input type="text" name="title" id="title">
      <label for="description">Description</label>
      <textarea name="description" rows="2" cols="30"></textarea>
      <input type="submit" value="Add Task">
    </form>

    {% for task in tasks %}
    <div>
      <p>
        {{ task.title }}: <b>{{ task.description }}</b>
        {% if task.done %}
        <span> &#9989;</span>
        {% endif %}
    </p>
    </div>
    {% endfor %}
{% endblock %}

```

So when we submit the form we will send a post request through which our controller file will handle.

In our new view we want to:

1. Create a new task using the data from the form
2. Add the new task
3. Render the updated task list.

Let's start by telling the controller that we will have a post request coming through.

As this needs to be a POST method we will inform the decorator of this. We can declare which methods are used for this route. This is passed as a list. We only want POST for this route. For now we will just return a string to make sure we can get this working.

```python
# controller.py

@app.route('/add-task', methods=['POST'])
def add_task():
  return "Done"
```

Next we need to access the form data to create the new task.

To access the form in our `controller.py` file we will need to get access to the request that is being made.

Fortunately for us Flask makes that simple. Flask comes with a request object that we can import into our file.

```python
# routes.py

from flask import render_template, request # MODIFIED
```

And now in our route we can access the form by calling request.form.

Let's print it out and see what we get.

```python
#routes.py

@app.route('/add-task', methods=['POST'])
def add_task():
  print(request.form)
  return 'Done'
```

IF we submit the form and look at the terminal we can see that the request.form is a type of dictionary, `ImmutableMultiDict`. The good news is that we can access the data like a normal dictionary. The keys in the dictionary relate to the `name` that we gave the input. So..

```html
<input type="text name="name"">
```

Would give us a key of `name` in the dictionary and the value would be whatever the user typed in.

We should see the form values as key value pairs. So we can access these using the keys and create a new task.

We will need to import the Task class at the top of the file as well. We will also import the `add_new_task` function from the todo list script.

```python
#routes.py

from app.models.todo_list import tasks, add_new_task # MODIFIED
from app.models.task import * # ADDED

@app.route('/add-task', methods=['POST'])
def add_task():
  taskTitle = request.form['title'] # ADDED
  taskDesc = request.form['description']
  newTask = Task(title=taskTitle, description=taskDesc, done=False)

  return 'Done'
```

Now we can add the task to our todo list. We can simply call the `add_new_task` function we imported.

```python
#routes.py

@app.route('/add-task', methods=['POST'])
def add_task():
  taskTitle = request.form['title']
  taskDesc = request.form['description']
  newTask = Task(title=taskTitle, description=taskDesc, done=False)
  add_new_task(newTask) # ADDED
  return 'Done'
```

Now that we have added it our tasks should be updated. We can now re-use the index template and re-render the list.


```python
#routes.py

@app.route('/add-task', methods=['POST'])
def add_task():

  taskTitle = request.form['title']
  taskDesc = request.form['description']
  newTask = Task(title=taskTitle, description=taskDesc, done=False)
  add_new_task(newTask)
  return render_template('index.html', title='Home', tasks=tasks) # MODIFIED
```

Now if we use the form to add the task we can see it in our list.

Unfortunately this isn't persisted so if we restart the server it will disappear.

Next week we will show you how we would save to a database so that our data will be persisted even if the server stops running.

## Summary

Templates allow us to separate the logic and presentation of our app.

We can pass any specific content of the back end to the view by creating key-value pairs passed into the render_template function.

These can be referenced inside our templates.

Jinja2 allows us to have more control in our templates with if and for loops.

Templates can inherit other templates to allow shared view content across multiple pages without duplicating the code.
