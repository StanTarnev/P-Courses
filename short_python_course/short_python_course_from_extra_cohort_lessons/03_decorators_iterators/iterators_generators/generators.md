# Generators

**Duration: 15 minutes**

## Learning Objectives

- Be able to write simple generator functions

### Intro

In Python, if we wanted to generate a sequence from zero to ten, we might do something like this:

```python
numbers = range(11)

for number in numbers:
    print(number)
```

You might think that `numbers` here is a list - we can loop over it, after all. However, every time we generate a `range` in Python3, we are really using a _generator_ function; something that knows how to generate the next value in a sequence. 

We can see this if we try to print out `numbers`:

```python
numbers = range(11)

# Added
print(numbers)
```

Notice that it is not a `list` that is printed out, but a `range`. This is a class of its own, not a `list`.

Using generators brings some benefits:

- The expression is _lazily_ evaluated - it only generates the next value when it is needed
- The expression allows us to generate sequences of arbitrary (infinite?) size

It also brings some drawbacks:

- We can't slice, append, insert, remove etc. - we're not working with a list!

### Writing our own generator

In order to write our own generator, we have to get familiar with the `yield` keyword. `yield` allows us to - effectively - return more than one value from a function.

Let's say that we wanted to write a generator function to give us all of the even values up to `n`. Our code might look something like this:

```python
def generate_evens(n):
    i = 0
    while i < n:
        if i % 2 == 0:
            yield i
        i = i + 1

for number in generate_evens(10):
    print(number)
```

If we _do_ want a list, we can convert the result of a generator function by calling `list()` on it. For example:

```python
# Added
print(list(generate_evens(10)))
```
