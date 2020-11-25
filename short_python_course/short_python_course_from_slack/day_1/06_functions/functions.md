# Functions

**Duration: xx minutes**

## Learning Objectives

- Be able to define and use a function in Python
- Be able to define and use formal and actual parameters
- Be able to pass and use positional arguments, default arguments, and keyword arguments
- Be able to unpack lists and dictionaries into arguments
- Be able to pass an unlimited number of positional and keyword arguments

## Introduction

In Python, as in other programming languages, we can define functions that will allow us to re-use code as needed. We can also take in arguments / parameters, do something with them, and return values as needed.

But functions in Python have a number of special features that let us do some really interesting things with them - they are considered _first class objects_, which means that functions can be assigned to variables, or even returned from other functions. As developers, this opens up a lot of possibilities for us!

### Defining a function

Create a new file called `functions.py`

At its most basic, Python functions are defined as follows:

```python
# functions.py

def say_hello():
    return "hello world"

print(say_hello())
```

So in the function `say_hello`, we're returning the String "hello world", for our `print` function to print.

The most important thing to note here is that we need to indent our code, just as we did for `if` statements and `for` loops.

Of course, our functions might get a little bit more complex than `say_hello` - if we have an `if` statement or a `for` loop inside a function, we need to keep nesting our code further and further to the right.

For example:

```python
# functions.py

def set_alarm():
    day = "Monday"
    if(day == "Saturday" or day == "Sunday"):
        return None
    else:
        return "07:00"

print(set_alarm())
```

OK! So we've written a function that includes an if statement, and this works nicely. Well, not really. We've hard-coded the value "Monday" into the function, so it's always going to return "07:00". We can fix this by passing the day variable into the function. But how do we do this?

### Formal and actual parameters

The term _formal parameter_ is how we refer to a variable as found in the _definition_ of a function. They are placeholder names, that have no bearing on the name of the variable being handed to the function. You may see these being referred to as simply _parameters_.

_Actual parameters_ are the variables being passed into a function at the point of a function being called. You might also see these referred to as _arguments_.

### Positional arguments

Let's add the `day` variable as a formal parameter to `set_alarm`.

```python
# functions.py

# ADDED - day parameter
def set_alarm(day):
    if(day == "Saturday" or day == "Sunday"):
        return None
    else:
        return "07:00"

print(set_alarm())
```

If we run this code now, we can see an error appearing: `TypeError: set_alarm() missing 1 required positional argument: 'day'`.

This error is being thrown because we've specified that `set_alarm` take in one formal parameter - `day`. We can fix this quite easily - by adding the actual parameter to our function call:

```python
# functions.py

print(set_alarm("Monday"))
```

But what is a "positional" argument? Here's another example - this time with two formal parameters - to demonstrate.

```python
# functions.py

def add(a, b):
    return a + b

result = add(2, 4)
print(result)
```

In this case, `a` takes the value of 2 inside the function, because it's the first formal parameter listed. And similarly, `b` takes the value of 4. Python relies on the _position_ of the formal parameters to decide what their values should be.

### Scope

Variables declared within functions cannot be seen outside of these functions unless they are returned.

```python
# functions.py

def say_hello():
    name = "Ali"
    print("Hi, " + name)

# NameError: name 'name' is not defined
print(name)
```

In many programming languages, functions only have access to variables that are passed in via formal arguments, or that are locally declared. This is not, however, the case in Python.

Consider the following.

```python
# functions.py

name = "Ali"

def say_hello():
    print("Hi, " + name)

say_hello()
```

Notice that the `say_hello` function can see the `name` variable, even though it is declared in the enclosing scope. This is called a _closure_.

We can overwrite this variable within the function - this is called _shadowing_ the variable.

```python
# functions.py

name = "Ali"

def say_hello():
    name = "Steph"
    print("Hi, " + name)

say_hello()

# The value of `name` is still "Ali" - it hasn't changed in this scope!
print(name)
```

Or, we could overwrite the variable by using an argument.

```python
# functions.py

name = "Ali"

def say_hello(name):
    print("Hi, " + name)

say_hello("Steph")

# The value of `name` is still "Ali" - it hasn't changed in this scope!
print(name)
```

These are all useful techniques in their own right, but the most important thing is to be aware of what variables are being declared and used.

### Default arguments

Python also allows us to set _default_ formal parameters - ones which are optional, but have a default value if they are not passed in as actual parameters.

```python
# functions.py

def add(a, b = 2):
    return a + b

result = add(2)
print(result)

result = add(2, 10)
print(result)
```

In this case, we _can_ use a different number of actual parameters when we call the function, because we've set a default value for `b`.

### Keyword arguments

We can also refer to the argument by their keyword, when we pass actual parameters. This means that we can do some really unusual things, like reversing the order we pass them in:

```python
# functions.py

def add(a, b = 2):
    return a + b

result = add(b = 3, a = 1)
print(result)
```

We can also mix positional and keyword arguments. Let's investigate further.

#### Task - 10 minutes

Given the previous function `add`, think through the following function calls. Try to work out what the result will be.

Then, execute each function call and print the result. Are the results as you expected?

1) `result = add(a = -2)`
2) `result = add(b = 3)`
3) `result = add(2, b = 4)`
4) `result = add(b = 4, 2)`
5) `result = add(a = 2, 4)`

Explanations:

1) Here, we're passing one keyword argument of `-2`. With the default argument of `b = 2`, this gives us `-2 + 2`, which is zero.

2) We get an error in this case - although we've specified a value for `b`, we haven't passed a value for `a`.

3) Here, we're passing both a _positional_ argument for `a`. and a _keyword_ argument for `b`, which overrides its default value.

4) This gives us an error - "positional argument follows keyword argument." In this case, Python isn't sure what you mean. Keyword arguments must _always_ follow positional arguments, if you are using both.

5) As in number 4, we've broken the cardinal rule that keyword arguments must come last. Even if it's "clear" what we intended to do, we still have to follow the rules.

## Conclusion

We've seen that Python offers a great deal of versatility in how we use functions and pass in variables as actual parameters.

Unlike other programming languages, we can change the order they are passed in, or vary the number of arguments.

This gives us a great deal of flexibility, and we'll see the some of these techniques further when we look at files and databases.
