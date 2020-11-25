# Variables and Types

**Duration: 30 minutes**

## Learning Objectives

- Be able to describe some of Python's types
- Be able to declare variables in Python

## Introduction

Just as in other programming languages, values have to belong to a certain _type_.

Python provides a number of [built-in](https://docs.python.org/3/library/functions.html) functions. We can tell what type a value is by using Python's built-in `type()` function. We'll see a few more built-in functions shortly.

> Task - 5 minutes: Create a new python file called types.py in the terminal.
 Use the `type()` function to investigate the types of the following values:

```python
# types.py

print(type("Hello World!"))
print(type(4))
print(type(4.0))
print(type(True))
print(type(False))
print(type(None))
```

In order, you should have found the following types:

### str / String

In Python 3, a string represents a collection of Unicode characters.

If we want to take a substring, we can use the slice syntax. To do this, we can take a string, put square brackets on the end, pass in the start point, and optionally, the number of characters to take.

```python
# types.py

print("Hello World!"[0])
print("Hello World!"[0:5])
```

It's important to note, however, that although we can access a substring using the slice syntax, we cannot reassign its value.

```python
# types.py

"Hello World!"[0] = "Y"
```

``TypeError: 'str' object does not support item assignment``

This is because strings in Python are _immutable_: you cannot change an existing string. We can however create new strings based upon our existing strings, through concatenation, for instance. We can concatenate strings with the `+` operator:

```python
# types.py

print("Hello" + " " + "World!")
```

We could find the length of a string by using the `len()` built-in keyword:

```python
# types.py

print(len("Hello World!"))
```

If we have a string of a single character, we can use the `ord()` built-in function to see its ASCII code:

```python
# types.py

print(ord("a"))
```

## int / Integer

Integers represent whole numbers, just as they do in other languages. (And in mathematics!)

We can perform arithmetic on integers and floats, as you would expect:

```python
# types.py

print(3 + 4)
print(5 - 2)
print(10 / 2)
print(5 * 4)
```

We can also use the modulus operator `%` to get the remainder of a division operation:

```python
# types.py

print(9 % 2)
```

> Task: What happens if you divide two integers that would leave you with a decimal number? What does `type(4 / 3)` return?

> Answer: We are left with a type of `float`.

We can convert integers to strings by using the `str()` built-in function, or to a float by using `float()`.

```python
# types.py

float(10)
str(10)
```

We can also convert integers to their equivalent ASCII characters by using the `chr()` built-in function.

```
chr(97)
chr(200)
```

> Note: `chr` actually returns the numeric code of whatever encoding you are currently working in - usually unicode rather than ASCII. But for our purposes, this difference is academic.

## float / Float

Floats represent decimal numbers.

To convert a float to an integer, we would use the `int()` function.

```
int(5.0)
int(5.7)
```

> Note: this does not perform rounding, but simply takes the integer part of the float.

## bool / Boolean

Booleans represent true and false values, and once again, are used similarly to other languages.

The capitalisation is important: only `True` and `False` are of type `bool`.

## NoneType / None

This is a special type that represents the _absence_ of a value. You might be familiar with this concept from other languages - Ruby has `nil`, Java and JavaScript has `null`, and just to be different, Python has `None`.

> Quiz: ask the class - what will the following print out?

```python
# types.py

print(type("42"))
print(type("42.0"))
print(type(1 + 2.4))
print(type(1 == 1)) # hard!
print(type(2 == 4))
```

This isn't an exhaustive list of types in Python. In particular, we haven't looked at collections yet. Don't worry, we'll see them soon!

## Declaring variables

Python is a *dynamically typed language*. One of the implications of this is that we don't have to specify what type a variable is when we declare it; we simply use an equals sign to assign a value to a variable name.

In addition, we don't need to declare variables before assigning them. We can just use them straight away.

> Instructor note - start a new script in IDLE

As we saw before, we can do something like this:

```python
# types.py

my_name = "Alan"
print(my_name)
```

Because Python is dynamically typed, there's nothing to stop the type of a variable from changing:

```python
# types.py

my_name = "Alan"
my_name = 5
print(my_name)
```

However, because Python is also _strongly_ typed, it will throw an error if we try to combine two incompatible types. We can't add a `str` and an `int` together, for example:

```python
# types.py

my_variable = "5" + 10
print(my_variable)
# TypeError: must be str, not int
```

One more nice little thing that Python allows: we can define more than one variable at a time:

```python
# types.py

a, b = 10, 5

print(a)
print(b)
```

### Task - 5 minutes

Declare three variables - `first_name` (String), `last_name` (String), and `year_of_birth` (Integer).

Create another variable - `username`, whose value is the first three letters of the person's first name, concatenated with the first three letters of their last name, concatenated with their year of birth.

Don't worry about capitalisation for now.

Solution:

```python
# types.py

first_name = "Barack"
last_name = "Obama"
year_of_birth = 1961

username = first_name[0:3] + last_name[0:3] + str(year_of_birth)

print(username)
```

## Conclusion

We saw that variables in Python must belong to a _type_, which describes the type of data that they store. We also saw how to set a variable in Python.

Python also provides us with a number of different data structures, just like other languages. Let's continue by taking a look at some of these.
