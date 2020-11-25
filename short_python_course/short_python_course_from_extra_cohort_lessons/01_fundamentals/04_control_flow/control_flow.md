# Control Flow

**Duration: 60 minutes**

## Learning Objectives

- Be able to use `if`, `elif` and `else` in Python
- Be able to use `for` and `while` loops
- Be able to use `break` and `continue` to control how loops operate
- Be able to write list comprehensions as an alternative to using loops and conditionals

## Introduction

In Python, as in other languages, our programs will generally execute one line after the other.

However, we can control the flow of our program in various ways - executing blocks of code conditionally, or doing things multiple times.

In this lesson, we're going to investigate how to use some of Python's built-in keywords to control how our program executes.

We're also going to see one of Python's most unusual features - its use of indentation to denote what a block of code is.

## Loops

In programming, we often need to run the same piece of code more than once. There are several common situations where this might be the case:

- Doing something once for every item in a list
- Doing something a set number of times
- Doing something while a condition evaluates to `True`

Let's take each of them in order.

### `for` loops

In the first two situations above, you would use Python's `for` loop:

```Python
shopping_list = ["milk", "bacon", "eggs"]
for item in shopping_list:
    print(item)
```

Python uses _whitespace_ to denote what code should be executed if the condition evaluates to true. So our print statement _must_ be indented to the right.

In this case, the `print` statement is indented to the right, because this statement belongs to the `for` loop.

If we mess up, and de-indent the code that should live inside the `for` loop, we get an error:

```python
shopping_list = ["milk", "bacon", "eggs"]
for item in shopping_list:
# CHANGED
print(item)
```

This gives us `IndentationError: expected an indented block`. If we want to fix this, we need to make sure that the `print` statement is indented to the right.

Let's fix this, and take it a step further.

```python
shopping_list = ["milk", "bacon", "eggs"]
for item in shopping_list:
    print(item)
# ADDED
print "That's the end of the shopping list!"
```

We can jump back to the left of the file to continue our program.

If we want to execute a block of code multiple times, we can do something like this:

```python
for x in range(1, 11):
    print(x)
```

In Python 2, `range(1,11)` effectively returns a list with the numbers 1 - 10 in it. In Python 3, it returns something slightly different, but you can consider it to be more or less the same thing.

> Instructor note: in Python 3 it produces an iterator - a lazily-evaluated list, which only generates values as they are needed.

### `while` Loops

Finally, we might want to run a block of code while some condition evaluates to `True`. For example:

```python
while(True):
    print("This will loop forever!")
```

> Instructor note: press ctrl-c to interrupt!

In reality, rather than specifying the condition as `True`, which would lead to an infinite loop, you might find that you need need to use an expression here, which will evaluate to `True` or `False`:

```python
counter = 0
while(counter < 10):
    print(counter)
    counter = counter + 1
```

Let's take a closer look at some of the different ways we can check conditions in Python.

## Conditionals

In Python, we can execute code conditionally by using the keywords `if`, `elif`, and `else`.

Let's see this in action.

> Create a new script in IDLE

```python
today = "Saturday"

if today == "Saturday":
    print("Let's have a long-lie!")
```

So in this case, we're using the `if` keyword, and the `==` operator to check if the value of the variable `today` matches `"Saturday"`.

We also have access to the following operators:

| Operator | Description | Example | Explanation |
| :------: | :---------: | :-----: | ----------- |
| == | Is equal to | a == b | `True` if both elements are the same |
| != | Is not equal to | a != b | `True` if the elements are not the same |
| <> | Is not equal to | a <> b | `True` if the elements are not the same. (Python 2 only) |
| > | Is greater than | a > b | `True` if `a` is greater than `b` |
| < | Is less than | a < b | `True` if `a` is less than `b` |
| >= | Is greater than or equal to | a >= b | `True` if `a` is greater than or equal to `b` |
| <= | Is less than or equal to | a <= b | `True` if `a` is less than or equal to `b` |

We can also chain conditions together using `and` or `or`:
```python
# Changed
today = "Sunday"

if today == "Saturday" or today == "Sunday":
    print("Let's have a long-lie!")
```

Just like in our loops, we need to indent the code that belongs to the `if` statement.

Taking this a step further, we can specify what should happen when the condition evaluates to `False`:

```python
# Changed
today = "Monday"

if today == "Saturday" or today == "Sunday":
    print("Let's have a long-lie!")
# ADDED
else:
    print("Oh no! It's a work day!")

print("This will print out regardless!")
```

Notice that we move the indentation of the `else` to be aligned with the `if` statement, and the `print` statement is indented so that it belongs to the `else`.

Finally, we can use the if...elif...else structure if we want to do something based on a variety of possibilities.

```python
today = "Friday"

if today == "Saturday" or today == "Sunday":
    print("Let's have a long-lie!")
elif today == "Friday":
    print("It's almost the weekend!")
else:
    print("Oh no! It's a work day!")

print("This will print out regardless!")
```

You might find that other languages have different constructs to deal with this situation - `case` statements, `switch` statements; Python has none of these.

Python does, however, use a concept called "list comprehensions". These allow us to combine loops and conditionals to create new data structures. Let's take a look.

### List comprehensions

List comprehensions allow us to build lists in a way that is concise, elegant, and _Pythonic_.

Let's imagine we have a list of numbers, and we want a list full of the _even_ numbers multiplied by themselves. (So we need the square of each even item in the list.)

We pretty much know how to do this already, doing something like this:

```python
# Remember, this effectively gives us a list of [1,2,3,4,5,6,7,8,9,10]
numbers = range(1, 11)
evens_squared = []
for number in numbers:
    if number % 2 == 0:
        evens_squared.append(number * number)

print(evens_squared)
```

Comprehensions allow us to re-write blocks of code, like the above, in a single line. The basic syntax goes something like this:

```python
evens_squared = [expression for item in list if condition]
```

This syntax might look strange, so let's break it down to make it nice and clear. We'll start with a a list of numbers, from 1 - 10.

```python
numbers = range(1, 11)
evens_squared = []
print(evens_squared)
```

Firstly, we write a set of square brackets, to announce that we're simply creating a new list. Next, we need something to loop over - in this case, our `numbers` list.

```python
numbers = range(1, 11)
evens_squared = [number for number in numbers]
print(evens_squared)
```

If we execute the code at this point, we'll see that we've looped over one list to create another - exactly the same as the first! Let's take it up a notch. We'll multiply the number by itself:

```python
numbers = range(1, 11)
evens_squared = [number * number for number in numbers]
print(evens_squared)
```

So our "expression" here is `number * number`. Let's add a condition next:

```python
numbers = range(1, 11)
evens_squared = [number * number for number in numbers if number % 2 == 0]
print(evens_squared)
```

And finally - to fulfil the promise of "a single line of code", we can remove the first line, too:

```python
evens_squared = [number * number for number in range(1, 11) if number % 2 == 0]
print(evens_squared)
```

So we've taken five lines of code - with a loop and conditional - and condensed it to one.

### Exercises: 15 minutes

**Part 1**

Using a loop, and the following list:

```python
ages = [5, 15, 64, 27, 84, 26]
```

- Find the sum total of the values in this list
- Find the average (mean) value of the items in the list

**Part 2**

Using a single list comprehension, and the following list:

```python
words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
```

- Build a new list, with the first letter from each word
- Convert each letter to lower case

Expected output: `["t", "q", "b", "f", "j", "o", "t", "l", "d"]`

**Hint:** Strings in Python work as if they were a tuple full of characters. How would you get the first element from a tuple or list?

**Part 3**

Implement a basic linear search algorithm using Python's `for` and `if` keywords.

Given the following data structure:

```python
pupils = ["Alison", "James", "Stephen", "Mandy", "Henry"]
```

Search through the list and check if the name "Jack" is included. Print out an appropriate message.

### Solutions

**Part 1**

```python
ages = [5, 15, 64, 27, 84, 26]

total = 0
for age in ages:
    total = total + age

print(total)

# Or increment a counter within the loop if they haven't seen `len()`
average = total / len(ages)
print(average)
```

**Part 2**

```python
words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
letters = [word[0].lower() for word in words]

print(letters)
```

**Part 3**

```python
pupils = ["Alison", "James", "Stephen", "Mandy", "Henry"]
found = False
for name in pupils:
    if name == "Jack":
        found = True

if found:
    print("Jack is in the list!")
else:
    print("Jack is not in the list!")
```

## Conclusion

We've seen that we can use loops and `if` statements to control the flow of our programs.

Loops also save us having to repeat the same piece of functionality in our code many times. Staying on the same theme, let's look at functions, and their use in Python.
