# Introduction to Object Oriented Programming

**Duration: 1 hour**
## Learning Objectives

- Be able to write a class in Python with properties and methods
- Be able to use class while processing data

## Introduction

Earlier, we saw that we can use `namedtuple` as an _immutable_ data structure.

Immutability brings a number of benefits - most notably a sense of safety, as we can't accidentally modify the data we're processing. However, it brings drawbacks too.

We saw that if we _do_ want to modify the contents of a `namedtuple`, we have to create a new instance with the old values, and write this back to the file.

We could also use _object oriented programming_ to achieve the same result in a more intuitive way.

Object oriented programming is the practice of using code to model real-world things - a user, a database server, or an oscar winner. We declare a blueprint - or _class_ - which can then be used to create _instances_ of that class.

Let's look at an example.

## Our first class - Instance Variables

Let's say that we wanted to create a `Person` class. What are some of the characteristics that each unique person has?

We could think about some of the following:

* name
* age
* height
* weight
* hair colour

...And so on. In the process of creating our program, we would decide which elements were necessary and useful for us.

Once we decide which things we care about, we can track these values as _instance variables_. That is, variables that belong to each instance of the `Person` class - each unique person.

Let's look at how we might model a person in Python. We'll say that - for now - we're only interested in two characteristics - a person's name, and their age.

> Create a new file called person.py

Firstly, we declare the blueprint - or _class_ - with the `class` keyword, followed by the name of the class. We'll follow the standard naming convention of using capitals for each word in the class' title..

(For example, `Person`, `Car`, or `FoodItem`.)

```python
# person.py

class Person:
```

Next, we have to declare a function which will run each time we create a new instance of a `Person`. Different languages have different syntax for doing this, but in Python, we need to define the `__init__()` method.

> n.b. We don't need to explicitly call this method - it is called for us automatically when we create a `Person`!

```python
# person.py

class Person:
	# ADDED
	def __init__():
```

As usual, we will need to indent this function to indicate that it belongs to the `Person` class.

So in this function, we can do whatever we need to do to set up an instance of a `Person`. Typically, we'll use the constructor to set instance variables - in this case, a name and an age.

Let's start by stating that we'll pass these values in when we create an instance of the class. And in order for the class to "remember" these variables, we'll need to store them on the instance of the class, which is indicated by the `self` keyword.

```python
# person.py

class Person:
	# CHANGED
	def __init__(name, age):
		self.name = name
		self.age = age
```

Now that we've defined our blueprint - our class - we can use it to _instantiate_ a particular person. Me, or you, or whoever we like.

We can do this like so:

```python
# person.py

# ...
new_person = Person("Charlotte", 45)
```

However, if we run this code, we'll find that we have an error: `TypeError: __init__() takes 2 positional arguments but 3 were given`.

What's going on here?

You can see in our constructor that we've referred to `self.name` and `self.age` - the `self` part refers to the unique instance of the class. In order for this to work - for us to attach variables to the instance of the class, we have to pass it in to `__init__`, like this:

```python
# person.py

class Person:
	# CHANGED
	def __init__(self, name, age):
		self.name = name
		self.age = age
```

Confusingly, we don't need to pass in this variable when we create an instance of the class - this should work:

```python
# person.py

new_person = Person("Charlotte", 45)
```

Be aware that when you write a function on a class in Python, it will **always take self as the first argument**.

Now that we've got our class up and running, we can get the instance variables back again quite easily:

```python
# person.py

print(new_person.name)
print(new_person.age)
```

## Our first class - functions

We saw that objects can track their state through _instance variables_. In addition to this, classes can also define behaviours - things that instances of that class should be able to do.

This works by giving the class a function - or in OOP parlance, a _method_.

```python
# person.py

class Person:
  # ...snip...
	# ADDED
  def talk(self):
    return "Hi there!"

# ADDED
new_person = Person("Charlotte", 45)
print(new_person.talk())
```

Notice that we're passing in `self` when we define the method, once again. And since we have access to the instance of the class, we can use use its instance variables within its methods, if we want:

```python
# person.py

def talk(self):
	# CHANGED
	return "Hi, my name's " + self.name + "!"
```

Just be careful - all of the usual rules regarding types will apply, so if we want our person to say their age, we need to convert their age to a string first.

```python
# person.py

def talk(self):
	return "My name is " + self.name + ", and I am " + str(self.age) + " years old!"
```

## Task

Create a class that models a car. A car should have the following instance variables:

* Make (String)
* Model (String)
* Top Speed (Int)

And it should have the following methods:

* start (which should return an appropriate String - such as "Brrmm Brrm!")

Make sure you can create an instance of your class and start your car.

Solution:

```python
# car.py

class Car:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed

    def start(self):
        return "Brmm Brmm!"

ford = Car("Ford", "Fiesta", 120)
print(ford.start())
```

## Conclusion

OOP can be a powerful tool that we can use in our programs. Let's take a look at a practical application of this concept.
