# Handling files with OOP

**Duration: 90 minutes**

## Learning Objectives:

- Be able to use a class within a practical application

## Introduction

We saw in the OOP lesson that we can use classes to provide quite a well formatted, fixed data structure.

Let's take advantage of these features to work with a CSV file, a type of data which has a very fixed format.

## Modelling our data

[Download this CSV file and rename it to "oscars.csv"](oscars.csv).

This is the list of all of the winners of the "Best Winner" Oscar, going back to 1928. It also contains the winner's age when they won the Oscar.

If we want to model each winner result as an instance of a class, these should be the instance variables that our class will use!

We're also going to be using the csv library here. (We could work without it, but again, it makes life a little easier.)

> Create a new file called `winner.py` and open in Atom

```python
# winner.py

import csv

class Winner:
  def __init__(self, index, year, age, name, movie):
    self.index = int(index)
    self.year = int(year)
    self.age = int(age)
    self.name = name
    self.movie = movie
```

One important thing we have to do here: we have to convert the age and year to an `int`. When we read each winner's age and year out of a CSV file, it will be a `string`, so we have have to manually convert it as appropriate.

## Processing the data

Let's say that we want to process the data in some way, amending some, or all of the rows. We'll start by reading all of the file data into a list, just as we did before.

We will set up an initially empty list to hold the winners we get back from the csv.

Sometimes CSV files can be produced with white space at the start of the lines (normally if people use spaces after the commas) so we can add a flag here to skip the initial space in the line.

```python
# winner.py

# After class definition
winners = []

with open("oscars.csv", "r") as csvfile:

```
There are at least three interesting things happening here:

* You might not have seen the with statement before; this makes sure that the file is closed again, once we're finished with it.

* `open` has a number of default parameters set, which controls how it behaves.

The `r` that we're passing in denotes that we want to open this file in read mode - this will happen by default whether we pass the r in or not, but it can be good to be explicit about what our intentions are.

Opening it in read mode means we can't amend the file at the moment, but this is fine for our purposes!

* Finally, we've now got a reference to the file we've opened in a variable called `csvfile`.

## Reading data

Let's continue. Our next job is to set up a `csv.reader` object. This will let us loop through each line of the CSV file. We use the `csv.reader()` function, that comes with the CSV library, and we pass in the file that we opened.

```python
# winner.py

# After class definition
winners = []

with open("oscars.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)

```

Great! Now that we're all set up, we can begin to loop through our reader object.

```python
# winner.py

# After class definition
winners = []

with open("oscars.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)

  for row in reader:
    print(row)
```

Here, we're printing out the row object. Let's try out this code - what do you see?

It looks like each row is a list. Great - we know how to work with that! At this point, we could actually complete our task just using `row[0], row[1]` etc. But let's make our code more readable, using our Winner class.

```python
# winner.py

# After class definition
winners = []

with open("oscars.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)

  for row in reader:
    current_winner = Winner(row[0], row[1], row[2], row[3], row[4])
```

And add the winner to the list of winners.

```python
# winner.py

# After class definition
winners = []

with open("oscars.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)

  for row in reader:
    current_winner = Winner(row[0], row[1], row[2], row[3], row[4])
    winners.append(current_winner)
```

And lastly print out each winners details.

We will use string formatting for this as we are including integers as well as strings (Concatenation won't work as will try to perform a mathematical `add` operation instead):

```python
# winner.py

# After class definition
winners = []

with open("oscars.csv") as csvfile:
  reader = csv.reader(csvfile, skipinitialspace=True)

  for row in reader:
    current_winner = Winner(row[0], row[1], row[2], row[3])
    winners.append(current_winner)

for winner in winners:
  print(f"{winner.name} won the oscar for {winner.movie} in {winner.year} aged {winner.age}")
```

If we run our program now, we actually get an error!

It is reading the first row in the CSV and trying to make a class. However the first row is the colum titles. So when it tries to convert the word `Index` to an int it fails.

There's a simple solution for this problem; we can just call the `next()` function on our `reader` instance to "fast-forward" past the first row.

```python
# Added
next(reader)
for row in reader:
```

Now if we run the program we should see the results printed out.

However, we still have quite a bit of ugliness in our program. This line, in particular, doesn't scale very well:

```python
current_winner = Winner(row[0], row[1], row[2], row[3], row[4])
```

What if we had a hundred columns in our CSV file? Would we have to type all the way to row[n]?

This is where the * operator comes in. The * operator unpacks lists into positional arguments. So we can refactor our program and simply do something like this:

```python
current_winner = Winner(*row)
```

Much neater!

## Writing to csv

Now that we've got a list of winner objects, we can open the file for writing, amend the objects as we need to, and write them to the file.

If we want to add a new line to the CSV, the first thing we'll need to do is figure out what index should be for the new line. To do this, we need a reader object, and we need to loop through the file, counting the number of rows.

```python
with open("oscars.csv") as csvfile:
    reader = csv.reader(csvfile)
    count = sum(1 for row in reader)
```

Next, we need to open the file in append mode, which we do by passing a parameter to open.
```python
with open("oscars.csv") as csvfile:
    reader = csv.reader(csvfile)
    count = sum(1 for row in reader)

with open("oscars.csv", "a") as csvfile: #Added
```

This time, rather than creating a reader object, we want a writer object, to write to the file.

```python
with open("oscars.csv", "a") as csvfile:
    # Added
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
```
This looks much the same as creating a reader object, but this time we also pass in an additional keyword argument: quoting. This ensures that each of the columns have their values properly quoted.

The next thing we should do is create a new `Winner` object, with 2020's winner:

```python
with open("oscars.csv", "a") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # Added
    winner = Winner(count, 2020, 50, "Renée Zellweger", "Judy")
```

Notice that we're passing in the count variable, which is the number of rows that we counted above.

Finally, we can append to the file by calling
`writer.writerow(data):`

Unfortunately, we can't simply pass the `winner` object to `writer.writerow`, as it belongs to a custom class that we have written. There are a number of ways to deal with this, and the simplest way is simply to pull the values out of the object into a list.


```python
with open("oscars.csv", "a") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    winner = Winner(count, 2020, 50, "Renée Zellweger", "Judy")
    writer.writerow([winner.index, winner.year, winner.age, winner.name, winner.movie])
```

Unfortunately, we can't simply pass the `winner` object to `writer.writerow`, as it belongs to a custom class that we have written. There are a number of ways to deal with this, and the simplest way is simply to pull the values out of the object into a list.

We can tidy this up a bit by writing a method on our `Winner` class, using `self`:

```python
# winner.py

# ...
def values(self):
  return [self.index, self.year, self.age, self.name, self.movie]
```

...And simply changing the call to `writer.writerow()` as follows:

```python
# winner.py

for winner in winners:
  # CHANGED
  writer.writerow(winner.values())
```

This should allow us to read and write to the file. The great thing about this is that we can edit each `winner` object freely.

If we wanted to increase everyone's age by one, we might do something like this:

```python
# winner.py

for winner in winners:
  # ADDED
  winner.age = winner.age + 1
  writer.writerow(winner.values())
```


## Changing rows in a file

> Comment out the code that writes the new winner to the file otherwise we will end up with duplicates

If we want to change the existing rows in some way, we need to call the open() function with the `w` option, for "write".

We need to be really careful doing this, because as soon as we call open("filename", "w"), Python truncates the file - it removes all of its contents!

How can we work around this?

> Task: 5 minutes: Ask the class for ideas

One way we can work around it would be to read all of the existing rows from our existing list first, then loop through that array, and write to the file again, making any changes we need to make.

Let's take a look at this.

In our earlier code to read all current rows into a list we have set up a winners list.

```python
with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile, skipinitialspace=True)
    next(reader)
    for row in reader:
        winners.append(Winner(*row))
```

We saw earlier that we have a list of all the winners read from the csv file.

Now we can just loop through this list, amending the row as needs be, and writing it back to the file. Let's look at the syntax for doing this.

```python
# oscars.py

with open("oscars.csv", "r") as csvfile:
    # AS BEFORE

with open("oscars.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    writer.writerow(["Index", "Year", "Age", "Name", "Movie"])

    for winner in winners:
        writer.writerow(winner.values())

for winner in winners:
    print(f"{winner.name} won the oscar {winner.movie} in {winner.year} aged {winner.age}")
```

If we check the file now, we should see that all the contents are there, but we haven't actually changed anything!

Let's say that we wanted to add 1 to each actress' age.

```python
# oscars.py

for winner in all_winners:
    # ADDED
    winner.age += 1
    writer.writerow(winner)
```
This works OK, but it's long-winded, inelegant, and a bit error-prone; all the things we don't want our Python programs to be.

If we only wanted a single entry to be updated we would need to get that entry based on some kind of condition (matching index, movie, etc).


### Mini-lab

Let's practice looping through and processing the data.

* Create a list with all of the winners from the 1980s
* Find the age of the oldest Oscar winner
* Create a list with all of Meryl Streep's Oscar winning movies

`Hint 1`: You can use either comprehensions or loops for these exercises. If you use comprehensions, you might find it easiest to build a list of all_winners first.

`Hint 2`: You might need to convert types - you can do so by calling int(value).

`Hint 3`: You can use slice syntax to check a substring - for example current_winner.year[0:3] will give the first three characters of the year.

### Solutions

Create a list with all of the winners from the 1980s:

Loop:

```python

with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    eighties = []
    for row in reader:
        if row[1][0:3] == "198":
            winner = Winner(*row)
            eighties.append(winner)

print(eighties)
```
List comprehension:

```python
eighties = [winner for winner in winners if str(winner.year)[0:3] == "198"]
```


Find the age of the oldest Oscar winner:

Loop:

```python
# ...
max_age = 0
    for row in reader:
        winner = Winner(*row)
        if winner.age > max_age:
            max_age = winner.age
```

Comprehension:

```python
max([winner.age for winner in all_winners])
```      

Create a list with all of Meryl Streep's Oscar winning movies.

Loop:
```python
# ...
streep_movies = []

    for row in reader:
        winner = Winner(*row)
        if winner.name == "Meryl Streep":
            streep_movies.append(winner.movie)
```

Comprehension:

```python
[winner.movie for winner in all_winners if winner.name == "Meryl Streep"])
```


## Conclusion

Object Oriented Programming gives us a powerful tool to help us to model the real world in our programs.

In this lesson, you have seen how to construct classes, call methods on them, and use them to interact with an external resource. (A CSV file.)

We've seen how to work with files, and use objects, list comprehensions, and the * operator in a small program.
