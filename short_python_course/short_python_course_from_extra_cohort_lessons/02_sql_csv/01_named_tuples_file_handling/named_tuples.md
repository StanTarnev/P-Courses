# Named Tuples

**Duration: 30 minutes**

## Learning Objectives

- Understand what a named tuple is, and its benefits
- Be able to create a named tuple and access its values

## Introduction

One of the most common tasks in programming is opening a file, reading some data, and processing it in some way.

We're going to use a CSV file holding some information to practice these concepts. But before we do, we're going to look at another data structure; one that will make working with CSVs really straightforward: the `namedtuple`.

> Instructor note: This is a _very_ important point to emphasise. It should be well understood that this is "processing an array of records".

In other languages, you might have heard of a `record`; this is essentially the same thing - a data structure where we can refer to the various fields by name.

We're going to be looping over these records, and processing them,

Let's take a closer look.

## Part One - `namedtuple`

Yesterday, we saw how we can use a `tuple` as an immutable data structure. (Remember, immutable means we can't change the data once it's in there!)

Let's have a quick recap on basic tuples.

```python
person = ("Michael", 37, "Instructor")
```

Now, if we want to get any information back from this object, we need to use array-like syntax. So if we want to get the person's name back, we can do something like this:

```python
print(person[0])
```

This is OK, but it doesn't scale very well. What if we have a lot of fields to track? We'd have to constantly check back to make sure we were using the right field. It would be error-prone, hard to read, and worst of all, _ugly_.

If we remember our Zen of Python, beautiful is better than ugly, and readability counts. There must be a better way.

Enter the `namedtuple`.

First of all, to use a `namedtuple`, we have to import it. Although it comes with Python, it isn't available to use straight away.

We need to put this line at the top of our program:

```python
from collections import namedtuple
```

Now, we can create tuples that will have specific, named fields.

```python
Person = namedtuple("Person", "name age job_title")
```

Firstly, we're creating a new variable called `Person`. The capital letter is deliberate here - we are reminding ourselves that `Person` is now, effectively, a new type - like a String, or an Integer.

Next, we're using the `namedtuple()` function to create the `Person` type. When we use it, we have to pass two arguments:

- The name of the type we want to create (this is largely for Python's internal use)
- The fields we want to use, separated by spaces

Now, we can create instances of a `Person`, and grab their fields either by index, or by the name we set earlier.

```python
me = Person("john", 37, "instructor")
print(me.name)
print(me[0])

print(me.age)
print(me[1])

print(me.job_title)
print(me[2])
```

We can see that we're free to use either the index of the field, or its name.

We _must_ use all available fields when we create a `Person`, and we can't pass extra fields:

```python
you = Person("Jim", 40)
# Too few fields! missing 1 required positional argument: 'job_title'

you = Person("Jim", 40, "teacher", "Glasgow")
# Too many fields! takes 4 positional arguments but 5 were given
```

If we really need to, we can pass a `None` value into a `namedtuple`, but this should be avoided if possible.

```python
you = Person("Jim", 40, None)
```

We also can't change a person's details after they are set - the fields are immutable:

```python
me.name = "Bob"
# AttributeError: can't set attribute
```

## Conclusion

When we use tuples, and namedtuples, we can be relative sure of what we're working with. We know the fields won't have changed, and we know that we need to have every field present, otherwise we'll get an error.

This makes it suitable for a number of tasks, but in particular, they are great for reading data from files and databases. Let's take a look at how we might do something like that.
