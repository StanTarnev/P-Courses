
Data Structures

Duration: 45 mins
Learning Objectives

    Know how to use Lists, Dictionaries, and Tuples
    Be able to read the Python documentation to call methods on instances of these classes

Introduction

Most programming languages will allow you to collect variables together in different ways. In other programming languages, you might have seen arrays, hashes, maps, hashmaps, sets, lists…

Python has a number of collections we can use, but we’re going to look at three in particular: List, Dictionary, and Tuple.
Lists

Lists are very similar to what other languages call arrays.

In Python, We can declare a list in much the same way as we would declare another variable. We use a variable name, the equals sign, and then square brackets containing the values we want to hold.

    Create a new python file called lists.py.

# lists.py

my_list = ["spam", "ham", "eggs"]
my_number_list = [1, 3, 4, 6, 10]

We can access the various elements of the list by index - the position of the element in the list:

# lists.py

print( my_list[0] )
print( my_list[2] )

We can also access counting from the back of the list:

# lists.py

print( my_list[-1] )

    Instructor note - ask: what happens if we try to access an element that doesn’t exist?

But if we try to access an element that doesn’t exist, we’ll get an IndexError.

# lists.py

print( my_list[10] )

It can also be useful to slice a list - to take a section of it and return it. If we want the first two items of a list, for example:

# lists.py
print( my_list[0:2] )

This is a short-hand way of saying “start at position zero, and give me two items.”

To find out how many items a list contains, use Python’s len() method. (This also works other types of sequences, such as Strings, dictionaries, and tuples - which you will see soon.)

# lists.py

num_items = len(my_list)
print( num_items )

Python also has a handy sum() built in method to calculate the sum of a list:

# lists.py

total = sum(my_number_list)
print( total )

Working with list methods

Let’s set up a list with the following elements:

# lists.py

stops = ["Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket"]

And let’s say that we wanted to add “Edinburgh Waverley” to the end of the list.

If we take a look at Python’s List documentation, we can see that Python’s lists have a number of handy methods we can use to perform operations.

The first method listed is append() - this lets us add an item to the end of our list. So if we want to use an append method on the list, the syntax looks like this:

# lists.py

stops.append("Edinburgh Waverley")

And lets check that our list has been amended:

# lists.py

print( stops )

    Task: 10 minutes

Using the documentation for list methods, complete the following tasks:

    Add “Queen Street” to the start of the list
    Find out what index “Croy” is at in the list
    Add “Polmont” at the appropriate point (between “Falkirk High” and “Linlithgow”)
    Remove “Haymarket” from the list of stops
    Remove all items from stops

Answers

    Add “Queen Street” to the start of the list

stops.insert(0, "Queen Street")

    Find out what index “Croy” is at in the list

stops.index("Croy")

    Add “Polmont” at the appropriate point (between “Falkirk High” and “Linlithgow”)

stops.insert(4, "Polmont")

    Remove “Haymarket” from the list of stops

stops.remove("Haymarket")
# Or slice
stops = stops[0:-1]

    Remove all items from stops

stops.clear()

# In Python 2, we have to do the rather nasty...
del stops[:]

Tuples

It’s possible in Python to create a list containing items of different types. For example, we might want to collect data about a person in a list, such as their name, age, job title and whether or not they are a vegetarian:

    Create a new file called tuples.py

# tuples.py

person = ["Michael", 37, "Instructor", True]
print( person )

A list isn’t a great way to store this data, however. The data is collected, which is great, but we probably don’t ever need to insert or append new data here. We have these four data points about a person, and that’s that. Nor do we need to remove data, nor clear the person, nor use any of the list methods we’ve seen.

And if we don’t need any of the behaviour associated with lists, then we probably don’t need a list!

Python has another type of data structure designed for holding data of mixed types, where we don’t expect the data to change: the tuple.

A tuple looks very similar to a list, but with round brackets () in place of square brackets []:

# tuples.py
person = ("Michael", 37, "Instructor", True)
print( person )

Data stored in a tuple can be accessed in the same way we access data in a list, with an index inside square brackets:

# tuples.py

print( person[0] ) # => 'Michael'
print( person[2] ) # => 'Instructor'

But one day our person really, really wants a bacon roll. We want to update the Boolean value that tells us the person is a vegetarian to False:

# tuples.py

person[3] = False
print( person )

This gives us an error: TypeError: 'tuple' object does not support item assignment

Tuples are immutable data structures, unlike lists which are mutable. The data contained in a tuple cannot be mutated, or altered in any way.
Tuple methods

Tuples only have two methods available: count, which counts the number of occurrences of an object in a tuple; and index, which returns the index of an object inside the tuple:

# tuples.py

print( person.count("Michael") ) # => 1
fruits = ("apple", "apple", "banana", "banana", "banana", "tangerine")
print(fruits.count("banana") ) # => 3
print(person.index("Instructor") ) # => 2

As we said before, tuples can also be passed into Python’s built-in functions, like len:

# tuples.py

print(len(person)) # => 4

Dictionaries

    Create a new file called dictionaries.py

Lists are useful if we want to gather values in an ordered way. Tuples are useful if we want to gather values in a structured way. But it can become unwieldy to refer to a list or tuple’s values by their index number, and as we saw in The Zen of Python, “Readability matters.” If we want to associate values with easier means of identifying them, we can use Python’s Dictionary.

While we used square brackets to denote a list, we can use curly brackets to declare a dictionary. Values in a dictionary are referred to by a key:

# dictionaries.py

user = {"name": "Christine", "age": 40}
print( user )

Usually, the keys for our dictionary will be Strings, but they can also be numeric, and can even be tuples!

To get information back out of a dictionary, we can use square-bracket notation, similar to a list.

# dictionaries.py

print( user["name"] )

If we want to assign a new key and value to user, we can do so like this:

# dictionaries.py

user["email"] = "christine@example.com"
print( user )

We can also remove keys and values, using del as follows:

# dictionaries.py

del(user["email"])
print( user )

Collections of collections

So far we’ve filled our collections with simple data types - strings, integers and floats. But collections can hold really any data type we like, even other collections! For example, we could represent a band with a list of dictionaries:

# dictionaries.py

beatles = [
  { "name": "John", "instrument": "guitar" },
  { "name": "Paul", "instrument": "bass" },
  { "name": "George", "instrument": "guitar" },
  { "name": "Ringo", "instrument": "drums" }
]

We can then access a dictionary from the list with an index, then access a band member’s name with the key, all in one line:

# dictionaries.py

print(beatles[1]["name"]) # => "Paul"

    Task: 5 minutes.

Create a dictionary with the following information about yourself:

    Your name (a String)
    Your age (an Int - can be imaginary!)
    A list of your students. (These can also be imaginary!)

Make sure you can retrieve each field.

Answer:

# dictionaries.py

user = {
	"name": "John",
	"age": 37,
	"pupils": ["Gill", "Gerry", "Mike", "Sally"]
}

print( user )

“namedtuple”

Earlier, we saw how we can use a tuple as an immutable data structure. (Remember, immutable means we can’t change the data once it’s in there!)

    Create a new file called named_tuples.py and open in Atom

If we want to get any information back from a tuple, we need to use array-like syntax. So if we want to get the person’s name back from earlier, we would do something like this:

# named_tuples.py

print(person[0])

This is OK, but it doesn’t scale very well. What if we have a lot of fields to track? We’d have to constantly check back to make sure we were using the right field. It would be error-prone, hard to read, and worst of all, ugly.

If we remember our Zen of Python, beautiful is better than ugly, and readability counts. There must be a better way.

Enter the namedtuple.

First of all, to use a namedtuple, we have to import it. Although it comes with Python, it isn’t available to use straight away.

We need to put this line at the top of our program:

# named_tuples.py

from collections import namedtuple

Now, we can create tuples that will have specific, named fields.

# named_tuples.py

Person = namedtuple("Person", "name age job_title")

Firstly, we’re creating a new variable called Person. The capital letter is deliberate here - we are reminding ourselves that Person is now, effectively, a new type - like a String, or an Integer.

Next, we’re using the namedtuple() function to create the Person type. When we use it, we have to pass two arguments:

    The name of the type we want to create (this is largely for Python’s internal use)
    The fields we want to use, separated by spaces

Now, we can create instances of a Person, and grab their fields either by index, or by the name we set earlier.

# named_tuples.py

me = Person("john", 37, "instructor")
print(me.name)
print(me[0])

print(me.age)
print(me[1])

print(me.job_title)
print(me[2])

We can see that we’re free to use either the index of the field, or its name.

We must use all available fields when we create a Person, and we can’t pass extra fields:

# named_tuples.py

you = Person("Jim", 40)
# Too few fields! missing 1 required positional argument: 'job_title'

you = Person("Jim", 40, "teacher", "Glasgow")
# Too many fields! takes 4 positional arguments but 5 were given

If we really need to, we can pass a None value into a namedtuple, but this should be avoided if possible.

# named_tuples.py

you = Person("Jim", 40, None)

We also can’t change a person’s details after they are set - the fields are immutable:

# named_tuples.py

me.name = "Bob"
# AttributeError: can't set attribute

When we use tuples, and named tuples, we can be relative sure of what we’re working with. We know the fields won’t have changed, and we know that we need to have every field present, otherwise we’ll get an error.

This makes it suitable for a number of tasks, but in particular, they are great for reading data from files and databases. Let’s take a look at how we might do something like that.
Conclusion

We can use lists and dictionaries to gather information together. Python provides a number of different data structures that we can use, including Lists, Dictionaries, Tuples, and Sets.

    Task: 5 minutes. Using the Python 3 documentation on data structures, investigate what Sets are, and where they might be used.
