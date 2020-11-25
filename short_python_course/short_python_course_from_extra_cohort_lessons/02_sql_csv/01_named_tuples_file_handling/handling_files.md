# Named Tuples - A Practical Example

**Duration: 45 mins**

## Learning Objectives

- Be able to open and parse CSV files in Python, using named tuples

## Introduction

We saw in the previous lesson that we can use named tuples to provide quite a strict data structure, where fields cannot be amended, and we have to pass exactly the right number of fields.

Let's take advantage of these features to work with a CSV file, a type of data which has a very fixed format.

> Instructor note: Distribute oscars.csv (https://people.sc.fsu.edu/~jburkardt/data/csv/oscar_age_female.csv) - Note that if the students have to download the file from the internet, they will have to remove the commas in the "movie" field for 1928 and 1952!

This is the list of all of the winners of the "Best Actress" Oscar, going back to 1928. It also contains the winner's age when they won the Oscar.

We're going to open this file, loop through each line, process it, and write it back to the file again.

## Working with files

Firstly, lets start a new script in IDLE, and save it as `oscars.py`. We also need to store our CSV file in the same directory. It could be stored elsewhere, but this will make it a little easier to deal with.

Now, in our script, we want to make sure that we bring in `namedtuple` to work with. We're also going to be using the `csv` library here. (We could work without it, but again, it makes life a little easier.)

```python
from collections import namedtuple
import csv
```

Now that we've done that, we can open the CSV file to work with. We need to pass in at least one argument - the path to the file:

```python
# ...
# ADDED
with open("oscars.csv", "r") as csvfile:
```

There are at least three interesting things happening here:

You might not have seen the `with` statement before; this makes sure that the file is closed again, once we're finished with it.

`open` has a number of default parameters set, which controls how it behaves. The `r` that we're passing in denotes that we want to open this file in `read` mode - this will happen by default whether we pass the `r` in or not, but it can be good to be explicit about what our intentions are. Opening it in `read` mode means we can't amend the file at the moment, but this is fine for our purposes!

Finally, we've now got a reference to the file we've opened in a variable called `csvfile`.

### Reading data

Let's continue. Our next job is to set up a `csv.reader` object. This will let us loop through each line of the CSV file. We use the `csv.reader()` function, that comes with the CSV library, and we pass in the file that we opened.

```python
with open("oscars.csv", "r") as csvfile:
    # ADDED
    reader = csv.reader(csvfile)
```

Next, let's set up a `namedtuple` that will hold all of the information for our row. If we open the CSV file, we can see that we have fields for index, year, age, name, and movie. These are the fields we should pass to our `namedtuple` function. This data structure will hold all of the information for a single line in our CSV.

```python
# ...
with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile)

    # ADDED
    Winner = namedtuple("Winner", "index year age name movie")
```

Great! Now that we're all set up, we can begin to loop through our `reader` object.

```python
with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    Winner = namedtuple("Winner", "index year age name movie")

    # ADDED
    for row in reader:
        print(row)
```

Here, we're printing out the `row` object. Let's try out this code - what do you see?

It looks like each `row` is a list. Great - we know how to work with that! At this point, we could actually complete our task just using `row[0]`, `row[1]` etc. But let's make our code more readable, using a `namedtuple`.

```python
with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    Winner = namedtuple("Winner", "index year age name movie")

    for row in reader:
        # ADDED
        current_winner = Winner(row[0], row[1], row[2], row[3], row[4])
        print(current_winner.name + " won the oscar for " + current_winner.movie + " in " + current_winner.year)
```

If we run our program now, it should be working!

However, we still have quite a bit of ugliness in our program. This line, in particular, doesn't scale very well:

```python
current_winner = Winner(row[0], row[1], row[2], row[3], row[4])
```

What if we had a hundred columns in our CSV file? Would we have to type all the way to `row[n]`?

This is where the `*` operator comes in. The `*` operator unpacks lists into positional arguments. So we can refactor our program and simply do something like this:

```python
current_winner = Winner(*row)
```

Much neater!

To finish off our program, let's tidy up our output a little bit further. We have a few problems.

- The first line of our output is ""Name" won the oscar for  "Movie" in  "Year""
- We have a few unwanted double-quotes through our output
- We have some unwanted whitespace around the fields as they are being printed out

There's a simple solution for the first problem; we can just call the `next()` function on our `reader` instance to "fast-forward" past the first row.

```python
# Added
next(reader)
for row in reader:
```

As for the second and third points - these are things we can do in one step, using the power of list comprehensions.

So we need to do two things; strip whitespace, and remove double quotes. Let's start off our comprehension by writing one that simply returns the same column for each row. We can build it up bit by bit to let it do what we need to do.

Since `row` is just a list, we can loop over it to get each column - the movie star's name, their age etc. So something like this should just return each column, unchanged.

```python
for row in reader:
    row = [column for column in row]
    current_winner = Winner(*row)
```

Not much, but it's a start.

Let's take a moment to think about what we know about about `column`. We know that it's a String, and that means that we have a whole load of methods we can use on it!

> Task: 10 minutes

Read through the documentation for [Python's String objects](https://docs.python.org/3/library/stdtypes.html#string-methods), and see if you can find methods to remove whitespace, and remove particular characters.

Your final solution could look like this:

```python
from collections import namedtuple
import csv

with open("oscars.csv") as csvfile:
    reader = csv.reader(csvfile)
    Winner = namedtuple("Winner", "index year age name movie")
	next(reader)

	for row in reader:
        row = [column.strip().replace('"', "") for column in row]
        current_winner = Winner(*row)

        print(current_winner.name + " won the oscar for " + current_winner.movie + " in " + current_winner.year)
```

### Appending to a file

If we want to add a new line to the CSV, the first thing we'll need to do is figure out what index should be for the new line. To do this, we need a `reader` object, and we need to loop through the file, counting the number of rows.

```python
with open("oscars.csv") as csvfile:
    reader = csv.reader(csvfile)
    count = sum(1 for row in reader)
```

Next, we need to open the file in `append` mode, which we do by passing a parameter to `open`.

```python

with open("oscars.csv") as csvfile:
    reader = csv.reader(csvfile)
    count = sum(1 for row in reader)

with open("oscars.csv", "a") as csvfile: #Added
```

> Instructor note: If students are on a windows machine they need to use this line: `open("filename", "a", newline = '')` instead to stop python appending the new entry to the final row of the CSV file - without doing this the final row of the CSV file will be treated as a list with 10 elements, causing problems when trying to use it to make a Winner namedtuple.

This time, rather than creating a `reader` object, we want a `writer` object, to write to the file.

```python
with open("oscars.csv", "a") as csvfile:
    # Added
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
```

This looks much the same as creating a reader object, but this time we also pass in an additional keyword argument: `quoting`. This ensures that each of the columns have their values properly quoted.

The next thing we should do is create a new `namedtuple`, with 2017's winner:

```python
with open("oscars.csv", "a") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    # Added
    winner_2017 = Winner(count, 2017, 27, "Emma Stone", "La La Land")
```

Notice that we're passing in the `count` variable, which is the number of rows that we counted above.

Finally, we can append to the file by calling `writer.writerow(data)`:

```python
with open("oscars.csv", "a") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    winner_2017 = Winner(count, 2017, 27, "Emma Stone", "La La Land")
    # Added
    writer.writerow(winner_2017)
```

### Changing rows in a file

If we want to change the existing rows in some way, we need to call the `open()` function with the `w` option, for "write".

We need to be really careful doing this, because as soon as we call `open("filename", "w")`, Python _truncates_ the file - it removes all of its contents!

> Instructor note: Again, if students are on a windows machine they need to use this line: `open("filename", "w", newline = '')` instead to stop python adding an empty row below each entry.

How can we work around this?

> Task: 5 minutes: Ask the class for ideas

One way we can work around it would be to read all of the existing rows into an array first, then loop through that array, and write to the file again, making any changes we need to make.

Let's take a look at this.

We can amend our earlier code to read all current rows into a list. And we might as well remove the line printing out each row:

```python
with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    Winner = namedtuple("Winner", "index year age name movie")

    # ADDED
    all_winners = []    

    next(reader)

    for row in reader:
        row = [column.strip().replace('"', "") for column in row]
        current_winner = Winner(*row)

        # ADDED
        all_winners.append(current_winner)
```

If we `print(all_winners)` at this point, we should see that we've read all of the current rows into a list.

Now we can just loop through this list, amending the row as needs be, and writing it back to the file. Let's look at the syntax for doing this.

```python
with open("oscars.csv", "w") as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

    writer.writerow(["Index", "Year", "Age", "Name", "Movie"])

    for winner in all_winners:
        writer.writerow(winner)
```

If we check the file now, we should see that all the contents are there, but we haven't actually changed anything! This is where we run into the limitations of `namedtuple`s.

Because `namedtuple`s are immutable, we would need to create a new one if we wanted to modify any of its details. Let's say that we wanted to add 1 to each actress' age.

```python
for winner in all_winners:
    # ADDED
    new_age = winner.age + 1
    modified_winner = Winner(winner.index, winner.year, new_age, winner.name, winner.movie)
    writer.writerow(modified_winner)
```

This works OK, but it's long-winded, inelegant, and a bit error-prone; all the things we don't want our Python programs to be.

Later today, we'll look at how object-oriented programming can provide a better solution in circumstances such as this one.

## Mini-lab

Let's practice looping through and processing the data.

- Create a list with all of the winners from the 1980s
- Find the age of the oldest oscar winner
- Create a list with all of Meryl Streep's Oscar winning movies

Hint 1: You can use either comprehensions or loops for these exercises. If you use comprehensions, you might find it easiest to build a list of `all_winners` first.

Hint 2: You might need to convert types - you can do so by calling `int(value)`.

Hint 3: You can use slice syntax to check a substring - for example `current_winner.year[0:3]` will give the first three characters of the year.

### Solutions

Create a list with all of the winners from the 1980s:

List comprehension:

```python
[winner for winner in all_winners if winner.year[0:3] == "198"]
```

Loop:

```python
with open("oscars.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    Winner = namedtuple("Winner", "index year age name movie")

    next(reader)

    eighties = []
    for row in reader:
        row = [column.strip().replace('"', "") for column in row]
        current_winner = Winner(*row)
        if current_winner.year[0:3] == "198":
            eighties.append(current_winner)

print(eighties)
```

Find the age of the oldest oscar winner:

Comprehension:

```python
max([winner.age for winner in all_winners])
```

Loop:

```python
# ...
max_age = 0

for row in reader:
    row = [column.strip().replace('"', "") for column in row]
    current_winner = Winner(*row)
    if int(current_winner.age) > max_age:
        max_age = int(current_winner.age)
```

Create a list with all of Meryl Streep's Oscar winning movies.

Comprehension:

```python
[winner for winner in all_winners if winner.name == "Meryl Streep"])
```

Loop:

```python
# ...
streep_movies = []

for row in reader:
    row = [column.strip().replace('"', "") for column in row]
    current_winner = Winner(*row)
    if current_winner.name == "Meryl Streep":
        streep_movies.append(current_winner)
```

## Conclusion

We've seen how to work with files, and use `namedtuple`s, list comprehensions, and the `*` operator in a small program.

Let's practice some of these same principles.
