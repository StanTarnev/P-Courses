# Single models with databases

## Objectives

* Understand how Python talks to a database
* Know that an object maps to a row in the db table
* By the end of this lesson you should be able to create your own single model CRUD app (Python and SQL)

## Task Manager software

Today we are going to introduce this idea of persistence by creating software that tracks tasks

We want to be able to:

* Create new tasks
* Read/Find existing tasks
* Update existing tasks
* Delete existing tasks

Up until now most of this functionality would have been pretty hard to accomplish as we only had the computer's memory to use.

First of all though, we will setup our model and object - just like we have done many times in Week 2.

## Task/DB model

We are going to setup a model and it's role will be to speak to the database. We have created many models which are tested and each small method did something which we knew would work.

We could do the same for this Task DB model but it's more hassle than it's worth to test database models. It can be done but we aren't going to.

### Task Model

We are going to start with a class, representing a Task. A task has:

-  a description
-  the name of the person assigned to it
-  a duration
-  whether or not it has been completed (this will be False by default)


In terminal:

```bash
#terminal

mkdir models
touch models/task.py
```


```python

class Task:
    
    def __init__(self, description, assignee, duration, completed = False):
        self.description = description
        self.assignee = assignee
        self.duration = duration
        self.completed = completed
        
    def mark_complete(self):
        self.completed = True

```

Let's make a little file where we can play with our models.

```bash
#terminal

touch console.py
```

This is where we will create some instances of the tasks

```python
# console.py

import pdb 
from models.task import Task

task_1 = Task("Walk Dog", "Jack Jarvis", 60)

task_2 = Task("Feed Cat", "Victor McDade", 5)


pdb.set_trace()
```

quit - our tasks are gone!

## Adding a database

Great, now we can create instances of Tasks and we can create as many as we want but this is manual and time consuming. It would be nice to start talking to a database to handle all of our records.

### Mapping an instance to a table row

![Mapping Task Instance to Table Row](img/model_db_mapping.png)

We have a Task instance here with all the information we need about that task. If we wanted to save a record of our task, it would make sense to take those instance variable values and create a new row in our database table.

We will:

* Import a library, `psycopg2`, which allows us to: 
  - Make a connection to a database 
  - Execute a prepared SQL statement on that database
* Create a function, let's call it 'save', but it could be called anything e.g. persist_task etc.
* Write our SQL in our method and execute it
* Create a new task instance and invoke the save function

We can then check our table and see if it is has persisted.

### Creating a Database and table

```bash
#terminal

createdb task_manager
```

```bash
#terminal

mkdir db
touch db/task_manager.sql
```

in .sql we want to create our table to store our tasks. What do we want to save?

- description
- assignee
- duration
- completed

Basically all properties that we created in our Task class. We want to take these seperate inputs and save them as a new row in our database.

We want to differentiate between all our tasks, so what else might we add? An ID

```sql
-- db/task_manager.sql

DROP TABLE IF EXISTS tasks;

CREATE TABLE tasks (
  id SERIAL PRIMARY KEY,
  description VARCHAR(255),
  assignee VARCHAR(255),
  duration INT,
  completed BOOLEAN
);
```

In terminal:

```bash
#terminal

  psql -d task_manager -f db/task_manager.sql
```

* -d; database select
* -f; file to run in context of selected database

### The psycopg2 library

We now want to be able to get our Python code to communicate with our database. We are going to use a library to help us with this. This library will handle connecting to the database and will execute SQL for us.

We are using a PostgreSQL database so we need to use a library which has been written with this in mind. There are several libraries we could use but we are going to a library called [psycopg2](https://pypi.org/project/psycopg2/), which is the most popular. 

The psycopg2 library is not installed automatically when we install python so we need to install it. Can you remember which program we use to install Python libraries and packages? `pip3`.

So let's install psycopg2

```bash
# terminal

pip3 install psycopg2
```

So now we can use this library in our code to connect with our database and run SQL commands. Where shall we write this code. We could add methods to our `Task` class and run them there. That would be fine. But what if we wanted to change the database we were using, maybe one which does not use SQL. We would have to go in and change all the code in our `Task` class. More importantly, the responsibility of our `Task` class is model a task, not to save tasks to the database. 

What we are going to do is add a layer of code, called a `repository` between our model and our database. This layer will be responsible for taking interacting with the database.

![Repository Layer](img/model_repo_db.png)

As we have a different class for each model, we usually create a different repository for each model. So let's create a repository for our tasks:

```bash
#terminal

mkdir repositories
touch repositories/task_repository.py
touch repositories/__init__.py
```

In this repository file we are going to write the functions for the interactions with the database (*C*reate, *R*ead, *U*pdate, and *Delete*). These functions are going to fall into the same pattern:

1) Make a connection to a database

2) Execute a prepared SQL statement on that database

3) Close the connection to the database

4) Return the results (if needed)

So it looks like there may be a bit of repeated code in our functions, especially regarding steps 1 and 3. Rather than having the same code repeated in the functions in our repository, we can move this common code out into a helper function into which we simply pass in the SQL we want to run and it will return the results. We can even use this helper function if we add further models and corresponding repositories.

### Creating a SQL Runner

We are going to create a module to run our SQL, called `run_sql`. Since the code is in this file is purely for database interaction, we will place it in our `db` directory:

```bash
# terminal

touch db/run_sql.py
```


So first of all we need to import psycopg2 into our repository

```python
# db/run_sql.py

import psycopg2  # ADDED

```

The psycopg2 library has some helper functions which are not automatically imported when you import psycopg2. These helper functions are in a module called [psycopg2.extras](https://www.psycopg.org/docs/extras.html). We will be using some functionality from this module so we need to import it to. It is common to give this the alias `ext`

```python
# db/run_sql.py

import psycopg2  
import psycopg2.extras as ext  # ADDED

```

So now we can start writing our code. So how do we want to structure it? Is it going to be a class? We only really need to create a class if our repository is going to store data i.e. have state. Our file is only going to contain one function so we don't really need to create a class. It is going to be just a function which we can call. Therefore, it makes sense to make `run_sql` a module.

So let's create our function. Like the name of the file, we will call it `run_sql`. It will take two parameters, one for the SQL we want to run, and another for the values we want to run that SQL with. Sometimes we might not want to pass in any values e.g. if we are getting all the rows in a table, so we'll give `values` a default value.

```python
# db/run_sql.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):

```


#### Creating our database connection

To connect to our database we use a function from the psycopg2 library called `connect`. This takes a string as a parameter. This string contains information about the database we want to connect to and is known as a _connection string_. This string usually contains the following information:

- the location of the machine which is hosting the database
- the name of the database
- the login details for the database (username and password)

In our case, the database is on our local machines and we don't need a username and password to log in so in this case we only need to give the name of the database we are connecting to. 

```python
# db/run_sql.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):

    conn=psycopg2.connect("dbname='task_manager'")  # ADDED

```

Connecting to a database can raise an exception e.g. if the database is on a different machine, that machine may be down, or the login details may be wrong. In that case, let's place the code where we interact with the database within a `try` block. If an exception is raised then we want to 'catch' a specific type of exception, that is a `psycopg2.DatabaseError`. This is where something has gone wrong when interacting with the database. In this case we will print the error.

We will also add a `finally` block. The code inside this block will run regardless of whether or not the code we `try` to run executes as expected. In this block we want to close our connection to the database as we don't want to leave a database connection open. It might be that our code connects to the database OK but an exception is raised when running our SQL. In that case we want to close the connection. Most databases can only handle a set amount of connections at a time so if we stay connected to the database when longer than we need to then we may be preventing another application from connecting to it.

```python
# task_repository.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):

    try:
       conn=psycopg2.connect("dbname='task_manager'") 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error):
    finally:
        conn.close()

```

But, what if our connection to the database failed, then we cannot call the `.close` method. What we can do is set `conn` to `None` at the start of the function and only close our connection if it has been successfull i.e. it is not `None`:

```python
# task_repository.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None

    try:
       conn=psycopg2.connect("dbname='task_manager'") 
    except (Exception, psycopg2.DatabaseError) as error:
        print(error):
    finally:
        if conn is not None:
            conn.close()

```

The next thing we need to do is to define something called a __cursor__ to work with. A cursor is a control structure which lets us go through the records in a database. We get this cursor by calling the `.cursor` method on our connection.

By default in psycopg2, these use tuples to represent the data from the database, but we can use  `dict` which allow us to use something similar to  Python dictionaries instead. We do this using `DictCursor` from `psycopg2.extras`. We pass an argument called `cursor_factory`, setting it to `DictCursor` when calling the `cursor` method on our connection

```python
# task_repository.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    
    try:
        conn=psycopg2.connect("dbname='task_manager'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)   # ADDED

```

Now that we have our cursor set up, we can run the SQL statement passed into the function. To do this we call the `execute` method on our cursor. We give it two arguments, the `sql` and `values` passed into the `run_sql` function when it is called.

```python
# db/run_sql.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    
    try:
        conn=psycopg2.connect("dbname='task_manager'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)    
        cur.execute(sql, values)  # ADDED
```

So we have run our code on our database so you think that's our changes there permanently. But this is not the case. When we run the code on our database using psycopg2 it runs something called a __transaction__ on our database. These changes are not permanent until they have been committed as they can also be rolled back. So to make the changes made by running our SQL permanent, we need to call the `.commit` method on our connection

```python
# db/run_sql.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    
    try:
        conn=psycopg2.connect("dbname='task_manager'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)    
        cur.execute(sql, values)  
        conn.commit()  # ADDED
```

#### Getting the results

When we run our SQL to get the items from the database we want to access the results to see what we can back. To do this we call the `fetchall` method on our `cursor`:

```python
results = cur.fetchall()
```

This gets all the rows returned from running the query. This is normally returned as a list of tuples, but as we are using `DictCursor` we get a list of dictionary-like items back.

We will return this list at the end of the function, but just in case an exception is raised we will set `results` to be an empty list at the start of the function.

```python
# db/run_sql.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []  # ADDED
    
    try:
        conn=psycopg2.connect("dbname='task_manager'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()  # ADDED
        cur.close()           
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results # ADDED
```

Finally, we need to close our cursor(`cur`) otherwise it will continue to keep hold of resources on the database until the connection is finally closed. 

```python
# db/run_sql.py

import psycopg2  
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []
    
    try:
        conn=psycopg2.connect("dbname='task_manager'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)   
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()           # ADDED
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return results
```

We can now use this function in our `task_repository`

## Saving a new Task

So let's create our first function. We'll create a `save` method. This will take in a `Task` object and store its details in our `task_manager` database. We are going to use our `run_sql` function so we will need to import it.

```python
# task_repository.py

from db.run_sql import run_sql

def save(task):

```

We can now create the SQL for our `save` function. As we are saving a new item to the database we will use an `INSERT` statement. 

One way to create our SQL would be to create a formatted string, using string interpolation to pass in the relevant data from our task object:

```python
# task_repository.py

from db.run_sql import run_sql

def save(task):
    sql = f"INSERT INTO tasks (description, assignee, duration, completed) VALUES ( '{task.description}', '{task.assignee}', {task.duration}, {task.completed} )"  # ADDED
```

> note duration and completed don't need speechmarks

#### Prepared statements

Let's stop for a second! As much as we'd love to trust our fellow human beings that they won't commit anything nasty against our database, the reality is a bit grimmer.

> Ask if they heard about SQL injection attacks

Basically, an SQL injection attack is a type of attack (whoa) where the attacker's intention is to either retrieve or delete data from databases. We're not going to show you how to execute an SQL injection attack, let's just accept the fact that it's not that difficult, and we should protect our code from such attacks.

> Make sure there is no line break before the last closing bracket in the task_repository's save method. If in trouble, use the formatting above

A SQL injection attack could be executed like this:

```python
#console.py

#same as before

task_3 = Task("Fix Car", "'); DELETE FROM tasks; --", 120)

task_repository.save(task_3)

```

SQL injections happen when a method accepts any form of input from the user without sanitising said input. To protect agains such attacks, we can use something called a prepared statement.

A prepared statement is essentially an SQL query that has a 2 step execution, rather than one. First, we prepare a statement and give it a name, which is essentially a string, and the SQL statement we want to execute. Instead of giving the values directly with the SQL statement, however, we only give it placeholders, indicating the number of values we want to insert in the SQL query.

Once the statement is prepared, we want to execute said prepared statement, this time providing the values too.

This has a number of benefits:

* By sanitising the input, we defend against SQL injection attacks
* This also let's us add apostrophes in our text values (imagine what would happen to a value like `'Bob's Guitars'` in a SQL query!)
* Plus once efficiency is a main concern, for mass updates/saves, a prepared statement is considerably faster.

Luckily, the psycopg2 library gives us an easy way of creating prepared statements!

```python
# repositories/task_repository.py

from db.run_sql import run_sql

def save(task):
    sql = "INSERT INTO tasks (description, assignee, duration, completed) VALUES (%s, %s, %s, %s)"
    values = [task.description, task.assignee, task.duration, task.completed]
```

Instead of providing the interpolated attributes of our instance, we are just flagging for PSQL that there will be 4 values we'd like to insert, indicating it with the `%s`.

Once the statement with the placeholders are prepared, we execute it by providing it the same name as the one we gave it when we prepared it, plus the values as an list.
Be careful: the values in the list should be in the same order as the placeholders indicate! In our case: `task.description, task.assignee, task.duration, task.completed`!

We can then call our `run_sql` function, passing in both `sql` and `values`

```python
# repositories/task_repository.py
from db.run_sql import run_sql

def save(task):
    sql = "INSERT INTO tasks (description, assignee, duration, completed) VALUES (%s, %s, %s, %s)"
    values = [task.description, task.assignee, task.duration, task.completed]
    run_sql(sql, values)
```

We can do this for one of our tasks in our console file.

```python
# console.py
import repositories.task_repository as task_repository # ADDED

# same as before 

task_repository.save(task_1) # ADDED

pdb.set_trace()
```

Run console.py from terminal

exit from pdb and let's access our database.

In terminal:

```sql
psql -d task_manager
select * from tasks;
```

Brilliant, we have mapped a Python instance to a SQL table row.

Note that only `task_1` has been saved.

## Reading from the database

### Getting all the tasks

Now, we want to go the other way. We want to:

* Read/take from our db table
* map them to Python objects

We'll create a function called `select_all` in our `task_repository` to get all the rows in the `tasks` table in the database and return a list of task objects. The SQL will be a `SELECT` clause. Since we are simply getting all the rows in the table, we do not need to pass any values into the `run_sql` function, but we do want to get the rows the function returns

```python
# repositories/task_repository.py

def select_all():  # ADDED
    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

```

The `run_sql` function returns a list of dictionary-like objects, but we really want a list of task objects back. To get this we need to loop through the list of results, getting the information for each task from the dictionary like object, and then creating a list of task objects:

```python
# repositories/task_repository.py
from db.run_sql import run_sql

from models.task import Task #  ADDED

def save(task):
    # AS BEFORE

def select_all():  
    tasks = []  # ADDED - in case we get `None` back from run_sql

    sql = "SELECT * FROM tasks"
    results = run_sql(sql)

    for row in results:
        task = Task(row['description'], row['assignee'], row['duration'], row['completed'], row['id'] )
        tasks.append(task)
    return tasks

```


```python
# console.py

import pdb 
from models.task import Task
import repositories.task_repository as task_repository  

task_1 = Task("Walk Dog", "Jack Jarvis", 60)

task_2 = Task("Feed Cat", "Victor McDade", 5)

print(task_1.__dict__)

task_repository.save(task_1)

res = task_repository.select_all()  # ADDED

for task in res:
    print(task.__dict__)

pdb.set_trace()

```

Currently, this will throw an error, as we are passing in more arguments than Task is expecting. We therefore need to do some changes to our Task model to fix this:


#### Adding the id

In our database return we have the ID in the dictionary, it would be cool to to have that information in our `Task` instances as well.

```python
# models/task.py

class Task:
    
    def __init__(self, description, assignee, duration, completed = False, id = None):  # MODIFIED
        self.description = description
        self.assignee = assignee
        self.duration = duration
        self.completed = completed
        self.id = id   # ADDED


```

This is fine for when we get all of the orders in `select_all()` but we would also like to update the object we have when we save - it currently doesn't have an id. 

```python
# repositories/task_repository.py

def save(task):
    sql = "INSERT INTO tasks (description, assignee, duration, completed) VALUES (%s, %s, %s, %s) RETURNING *"  # MODIFIED
    values = [task.description, task.assignee, task.duration, task.completed]
    results = run_sql(sql, values)  # MODIFIED
    id = results[0]['id']           # ADDED
    task.id = id                    # ADDED
    return task                     # ADDED
```

Remember, the ID of an object is extremely useful - it's the only unique identifier we have between the rows.


### Getting one particular task 

There will be cases where we want to get one particular row back from the database. We use a `SELECT` SQL statement for this but also need a `WHERE` clause to get a unique row, so what is unique in each row we could use to search on? The ID.

The `run_sql` function returns a list of rows (even if there is only one matching row) so if `run_sql` does not return `None` (i.e. no matching rows found) then we just want the first item in the list returned. We can then use the data in that row to create a task object which the `select` function can return

```python
# repositories/task_repository.py

def select(id):
    task = None
    sql = "SELECT * FROM tasks WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        task = Task(result['description'], result['assignee'], result['duration'], result['completed'], result['id'] )
    return task
```

## Deleting All

Everytime we run our console file, we are adding a new task. Let's clean out the database everytime we run it!

```python
# repositories/task_repository.py

def delete_all():
    sql = "DELETE  FROM tasks" 
    run_sql(sql)

```

```python
# console.py

import pdb 
from models.task import Task
import repositories.task_repository as task_repository 


task_repository.delete_all()  # ADDED

# AS BEFORE

```

## Deleting One

As well as deleting all tasks, we probably also want to be able to delete a single task. Given a single task object in the database has an id then we can delete it from the database using that id.

```python
# repositories/task_repository.py

def delete(id):
    sql = "DELETE  FROM tasks WHERE id = %s" 
    values = [id]
    run_sql(sql, values)
```

## Updating

Lastly, we might want to update a model. When we do changes like this:

```python
# console.rb

task_1.mark_complete()
```

This is sitting temporarily on the little model in memory. No SQL has run to cause the database to update the entries, so it gets lost if we exit pdb. Therefore we need to create an `update` function, which takes in a task object and updates the relevant row in the database:

```python
# repositories/task_repository.py

def update(task):
    sql = "UPDATE tasks SET (description, assignee, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
    values = [task.description, task.assignee, task.duration, task.completed, task.id]
    run_sql(sql, values) 

```
Now let's add to our console.py to call our update method so that our database is updated with this new information.

```python
# console.rb

task_1.mark_complete()
task_repository.update(task_1)
```

## Conclusion

We are now able to map instances of our task objects written in Python to rows in our SQL database. We can write SQL statements in our Python code and using the `psycopg2` library, have our SQL statements run on the database.
