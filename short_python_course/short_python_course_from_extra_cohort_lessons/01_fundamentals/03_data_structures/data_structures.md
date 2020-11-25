# Data Structures

**Duration: 45 mins**

## Learning Objectives

- Know how to use Lists, Dictionaries, and Tuples
- Be able to read the Python documentation to call methods on instances of these classes

## Introduction

Most programming languages will allow you to collect variables together in different ways. In other programming languages, you might have seen arrays, hashes, maps, hashmaps, sets, lists...

Python has a number of collections we can use, but we're going to look at three in particular: `List`, `Dictionary`, and `Tuple`.

## Lists

Lists are very similar to what other languages call arrays.

In Python, We can declare a list in much the same way as we would declare another variable. We use a variable name, the equals sign, and then square brackets containing the values we want to hold.

Create a new python file called `lists.py`.

```python
# lists.py

my_list = ["spam", "ham", "eggs"]
my_number_list = [1, 3, 4, 6, 10]
```

We can access the various elements of the list by _index_ - the position of the element in the list:

```python
# lists.py

print( my_list[0] )
print( my_list[2] )
```

We can also access counting from the back of the list:

```python
# lists.py

print( my_list[-1] )
```

> Instructor note - ask: what happens if we try to access an element that doesn't exist?

But if we try to access an element that doesn't exist, we'll get an `IndexError`.

```python
# lists.py

print( my_list[10] )
```

It can also be useful to _slice_ a list - to take a section of it and return it. If we want the first two items of a list, for example:

```python
# lists.py
print( my_list[0:2] )
```

This is a short-hand way of saying "start at position zero, and give me two items."

To find out how many items a list contains, use Python's `len()` method. (This also works other types of sequences, such as Strings, dictionaries, and tuples - which you will see soon.)

```python
# lists.py

num_items = len(my_list)
print( num_items )
```

Python also has a handy `sum()` built in method to calculate the sum of a list:

```python
# lists.py

total = sum(my_number_list)
print( total )
```

### Working with list methods

Let's set up a list with the following elements:

```python
# lists.py

stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]
```

And let's say that we wanted to add "Edinburgh Waverley" to the end of the list.

If we take a look at [Python's List documentation](https://docs.python.org/3/tutorial/datastructures.html), we can see that Python's lists have a number of handy methods we can use to perform operations.

The first method listed is `append()` - this lets us add an item to the end of our list. So if we want to use an append method on the list, the syntax looks like this:

```python
# lists.py

stops.append("Edinburgh Waverley")
```

And lets check that our list has been amended:
```python
# lists.py

print( stops )
```

> Task: 10 minutes

Using the documentation for list methods, complete the following tasks:

1. Add "Queen Street" to the start of the list
2. Find out what index "Croy" is at in the list
3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
4. Remove "Haymarket" from the list of stops
5. Remove all items from `stops`

#### Answers

1. Add "Queen Street" to the start of the list

```python
stops.insert(0, "Queen Street")
```

2. Find out what index "Croy" is at in the list

```python
stops.index("Croy")
```

3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")

```python
stops.insert(4, "Polmont")
```

4. Remove "Haymarket" from the list of stops

```python
stops.remove("Haymarket")
# Or slice
stops = stops[0:-1]
```

5. Remove all items from `stops`

```python
stops.clear()

# In Python 2, we have to do the rather nasty...
del stops[:]
```

## Tuples

It's possible in Python to create a list containing items of different types. For example, we might want to collect data about a person in a list, such as their name, age, and job title:

Create a new file called `tuples.py`

```python
# tuples.py

person = ["Michael", 37, "Instructor"]
print( person )
```

A list isn't a great way to store this data, however. The data is collected, which is great, but we probably don't ever need to `insert` or `append` new data here. We have these four data points about a person, and that's that. Nor do we need to `remove` data, nor `clear` the person, nor use any of the list methods we've seen.

And if we don't need any of the behaviour associated with lists, then we probably don't need a list!

Python has another type of data structure designed for holding data of mixed types, where we don't expect the data to change: the _tuple_.

A tuple looks very similar to a list, but with round brackets `()` in place of square brackets `[]`:

```python
# tuples.py
person = ("Michael", 37, "Instructor")
print( person )
```

Data stored in a tuple can be accessed in the same way we access data in a list, with an index inside square brackets:

```python
# tuples.py

print( person[0] ) # => 'Michael'
print( person[2] ) # => 'Instructor'
```

Unlike other data structures though this data cannot be changed.

If we tried we would get an error.

Let's say Michael gets promoted to Senior Instructor.

If we try and change that entry in the tuple....

```python
# tuples.py

person[2] = "Senior Instructor"
print( person )
```

This gives us an error: `TypeError: 'tuple' object does not support item assignment`

Tuples are _immutable_ data structures, unlike lists which are _mutable_. The data contained in a tuple cannot be mutated, or altered in any way.

### Tuple methods

Tuples only have two methods available: `count`, which counts the number of occurrences of an object in a tuple; and `index`, which returns the index of an object inside the tuple:

```python
# tuples.py

print( person.count("Michael") ) # => 1
fruits = ("apple", "apple", "banana", "banana", "banana", "tangerine")
print(fruits.count("banana") ) # => 3
print(person.index("Instructor") ) # => 2
```

As we said before, tuples can also be passed into Python's built-in functions, like `len`:

```python
# tuples.py

print(len(person)) # => 4
```

## Dictionaries

Create a new file called `dictionaries.py`


Lists are useful if we want to gather values in an _ordered_ way. Tuples are useful if we want to gather values in a _structured_ way. But it can become unwieldy to refer to a list or tuple's values by their index number, and as we saw in The Zen of Python, "Readability matters." If we want to associate values with easier means of identifying them, we can use Python's `Dictionary`.

While we used square brackets to denote a list, we can use curly brackets to declare a dictionary. Values in a dictionary are referred to by a _key_:

```python
# dictionaries.py

user = {"name": "Christine", "age": 40}
print( user )
```

Usually, the keys for our dictionary will be Strings, but they can also be numeric, and can even be tuples!

To get information back out of a dictionary, we can use square-bracket notation, similar to a list.

```python
# dictionaries.py

print( user["name"] )
```

If we want to assign a new key and value to `user`, we can do so like this:

```python
# dictionaries.py

user["email"] = "christine@example.com"
print( user )
```

We can also remove keys and values, using `del` as follows:

```python
# dictionaries.py

del(user["email"])
print( user )
```

## Collections of collections

So far we've filled our collections with simple data types - strings, integers and floats. But collections can hold really any data type we like, even other collections! For example, we could represent a band with a list of dictionaries:

```python
# dictionaries.py

beatles = [
  { "name": "John", "instrument": "guitar" },
  { "name": "Paul", "instrument": "bass" },
  { "name": "George", "instrument": "guitar" },
  { "name": "Ringo", "instrument": "drums" }
]
```

We can then access a dictionary from the list with an index, then access a band member's name with the key, all in one line:

```python
# dictionaries.py

print(beatles[1]["name"]) # => "Paul"
```

> Task: 5 minutes.

Create a dictionary with the following information about yourself:

- Your name (a `String`)
- Your age (an `Int` - can be imaginary!)
- A list of your students. (These can also be imaginary!)

Make sure you can retrieve each field.

Answer:

```python
# dictionaries.py

user = {
	"name": "John",
	"age": 37,
	"pupils": ["Gill", "Gerry", "Mike", "Sally"]
}

print( user )
```

## Conclusion

We can use lists and dictionaries to gather information together. Python provides a number of different data structures that we can use, including Lists, Dictionaries, Tuples, and Sets.

> Task: 5 minutes. Using the [Python 3 documentation on data structures](https://docs.python.org/3/tutorial/datastructures.html), investigate what Sets are, and where they might be used.
