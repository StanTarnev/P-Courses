# Iterators

**Duration: 15 minutes**

## Learning Objectives

- Understand the purpose of iterators
- Be able to write your own iterator

## Intro

> Create a new file called `iterators.py` and open in Atom

We've already seen that we can loop over lists, as in most other languages:

```python
# iterators.py

for number in [1,2,3]:
    print(number)
```

In Python, we can use iterators to - essentially - loop over things that _aren't_ lists. What?! Why would we want to do this?

Sometimes it is useful to be able to treat non-list things as...well, `list`y. For example, we can do this with Strings:

```python
# iterators.py

for letter in "Hello World!":
    print(letter)

print("Hello World"[0:5])
```

How can we implement this functionality in our own classes?

### Writing our own iterators

In Python, an object is "iterable" - we can loop over it - if it implements two specific methods: `__iter__()` and `__next__()`.

#### `__iter__()`

The first of these methods should do any initial setup that needs to be done, then return an `iterator` object - which is something that implements `__next__()`.

#### `__next__()`

`__next__()` should return the next value in the sequence.

### Putting it all together

Let's write a class that represents a lottery machine.

It should:

- Generate 6 random numbers between 1 and 49
- Check whether the number has already been chosen

Firstly, let's import the `random` package. (To generate the numbers.)

```python
# iterators.py

import random
```

Next, let's create our class. We'll stub out the `__iter__()` and `__next__()`.

```python
# iterators.py

class LotteryMachine:
    def __iter__(self):
        pass

    def __next__(self):
        pass
```

> Instructor note: talk about `pass` here if you need to.

If you think back to earlier in the lesson, you'll remember that the `__iter__()` method does any initial setup we need, then it returns an instance of a class that implements `__next__()`. In this case, we want to initialise an empty list of numbers so that we can track any numbers that have already been selected.

```python
# iterators.py

class LotteryMachine:
    def __iter__(self):
        self.numbers = []
        return self

    def __next__(self):
        pass
```

That's it! In this case, because our `LotteryMachine` class implements `__next__()`, we can return the current instance of the class.

Next, we have to provide an implementation for `__next__()`.

```python
# iterators.py

    def __next__(self):
        if len(self.numbers) == 6:
            raise StopIteration
        else:
            number = random.randint(1, 49)
            if number not in self.numbers:
                self.numbers.append(number)
                return number
```

Again, the code here is pretty simple. Firstly, we check to see if we've reached 6 numbers selected. If we have, we call `raise StopIteration`, which halts a `for` loop - which we'll see in a moment.

If we haven't reached six numbers then we:

- Generate a new random number
- Check if it doesn't appear in the `self.numbers` list
- If it doesn't, we add it to the list

Finally - crucially - we then `return` the number. This makes it available to whatever is looping over the object.

Let's see this in action, by instantiating a new `LotteryMachine`:

```python
# iterators.py

machine = LotteryMachine()

for number in machine:
    print(number)
```

Another really important thing to note here: we're not looping over `machine.numbers`, we're looping over the machine directly. While we could populate a list, and loop over it, we get a little more control if we do it this way.

For example, if we wanted to display each number one at a time, we could this:

```python
# iterators.py

next_value = next(iter(machine))
print(next_value)
```

## Summary

Iterators give the power of loops to _any_ of our custom classes.
