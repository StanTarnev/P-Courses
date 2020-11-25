# Decorators
#
**Duration: 30 minutes**

## Learning Objectives

- Understand that functions in Python are first-class objects
- Be able to define higher-order functions
- Be able to create and use Decorators

## Introduction

Now that we've looked at functions, let's take a look at how they can be passed around in Python, and how we can use _decorators_ to extend the functionality of our methods without altering them.

At their most basic level, decorators provide a simple syntax for calling higher-order functions. Although not synonymous with Python, you will definitely encounter them in the wild.

### Building to decorators

>Instructor note: if appropriate, ask the class what they can tell us about higher-order functions first.

A _higher-order function_ is a function that takes a function as an argument, or returns a function. Because functions in Python are _first-class objects_ we can store them in variables or pass them into functions (as _callbacks_), much like we would any other string, number or type of any sort.

Let's remind ourselves what we mean by this:

#### First-class objects

```bash
  touch decorators.py
```

```python
def say_hello():
  return "Hello world!"

hi = say_hello

print(hi())

print(hi)
print(say_hello)

```

So here we have a function, `say_hello`, that we assign to the variable `hi`. We can then invoke hi with brackets as we would any other function. When we print out `hi` and `say_hello` without brackets, we can see that they both point to the same object: `<function say_hello at 0x108fc1268>`.

#### Higher-Order Functions and Callbacks

We can also pass a function as a variable (as a callback) into other functions, creating a higher-order function, like so:

```python
def function_caller(callback):
  return callback()

print(function_caller(hi))
```

#### Nesting functions

We can also _nest_ functions within functions, so that they only exist in the scope of the function they're defined in:

```python
def outer_function():
  def inner_function():
    print("Hello from the inner function")

  inner_function()

outer_function()

```

Note if we try and call `inner_function` outside of `outer_function`, we get an error. It is scoped within `outer_function`.

### Bringing it all together

And if we combine all of this, it means if we wanted to, we could write a function that takes in a function, wrap some more functionality around it to extend it, and then return the whole wrapped function:

```python

def make_pretty(callback):
    def wrapper():
        print("I am a decorated function!")
        callback()
    return wrapper

def ordinary():
    print("I am an ordinary function")

pretty = make_pretty(ordinary)

ordinary()
pretty()

```
This is essentially what decorators do - wrap some extra functionality around our methods without altering their original implementation. They even come with some extra syntactic sugar, so that we need only annotate the method we want wrapped in a decorator with the __"@"__ symbol (this is also known as "pie syntax"):

```python
@make_pretty
def ordinary():
    print("I am ordinary")

```

Now whenever we try to call `ordinary`, our decorator means that it will be passed to `make_pretty` and called.

### Chaining Decorators

Our methods can have more than one decorator:

```python
def make_pretty(callback):
    def wrapper():
        print("I am a decorated function!")
        callback()
    return wrapper

def doTwice(callback): //ADDED
    def wrapper():
        callback()
        callback()
    return wrapper

@doTwice //ADDED
@make_pretty
def ordinary():
    print("I am ordinary")

```

The order of our decorators does matter, as you can see if you switch `@doTwice` and `@make_pretty` around.

### How else can decorators be used?

Let's make a decorator that will time how long our functions take to run!

```python

import time

def timing_function(callback):
    def wrapper():
        time1 = time.time()
        callback()
        time2 = time.time()
        return "Time it took to run the function: " + str((time2 - time1)) + "\n"
    return wrapper

@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

print(my_function())

```

Our decorators aren't confined to living in the same file where they're required, either - let's move `timing_function` out to a module:

```bash
touch timing_function.py
```

```python
//timing_function.py

def timing_function(callback):
    def wrapper():
        time1 = time.time()
        callback()
        time2 = time.time()
        return "Time it took to run the function: " + str((time2 - time1)) + "\n"
    return wrapper

//decorators.py
from timing_function import timing_function

@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

print(my_function())

```

## Summary

We've seen how decorators can be created, and added to our methods to extend their functionality without altering them.
