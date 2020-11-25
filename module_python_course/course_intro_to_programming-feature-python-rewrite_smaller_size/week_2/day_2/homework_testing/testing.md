# Testing with Python

**Lesson Duration: 30 minutes**

### Learning Objectives

- Know what a test is
- Understand why we test our code
- Understand the three As of testing (Arrange, Act, Assert)
- Be able to use `unittest` to test Python functions

## What is a Test?

A test is exactly what it sounds like - something that verifies your code is working.

Let's say you write a function:

```python
def five():
    return 5
```

How do we know that this function is working properly? Sure, we can look at it, and see that it's working, but that only works while the logic is simple. Another thing we can do is actually run the code. Like this:

```python
print(five())

# 5
```

Now, whenever we want, we can run the code, and check that the correct thing is printed out. This is great.

But could we do better? This is software development, after all. Wouldn't it be ideal if we could write code that ran our code and checked it worked properly? That would be mind-blowingly cool. And that's exactly what we mean when we talk about testing our code.

By the end of this lesson we'll be able to write code that automatically verifies that our functions are working correctly.

## Why Should We Test?

When we write our code we want to make sure it works as we expected. Maybe this sounds obvious. So let's make an ever bigger claim. We can craft better code if it's tested.

We haven't really touched on the craft of writing code yet. When we talk about code craft we mean things like the ability to easily make changes to code without
worrying about introducing bugs, as well as the ability for other people to work on our code easily.

Having tests we can run ensures that if we break code by changing it we know instantly.
Therefore the quality of the code is instantly improved, even if the code itself is unchanged. It also means that someone new to our code can look at the tests to very quickly work out how the code works.

There are many approaches to testing our code but the principles are the same.
What we want to do is write code which expects some specific thing to happen.
These "expectations" are referred to as assertions. As our tests run, each assertion
will either pass or fail, and the result will be printed to the terminal.

Most programming languages have test suites and different ways of testing. We will use `unittest`, Python's built-in testing module.

## How Do We Test?

> Hand out start code and give the students a few moments to look over it

Open the project with your text editor and have a look around. The first thing that you'll notice when looking at this project is likely that it is structured a little differently than usual. We have three files - calculator.py, calculator_test.py and run_tests.py. We also have two directories - src and tests.

```
├── run_tests.py
├── src
│   └── calculator.py
└── tests
    └── calculator_test.py
```

The src directory will contain our source code, the code that makes our program work. This is the code that needs to be tested. The tests directory will contain the code that checks if our source code works the way that we expect it to. run_tests.py will be responsible for running all of the tests within our tests directory.

calculator.py contains 4 functions, which have already been completed - `add`, `subtract`, `divide` & `multiply`. In this lesson we will write tests for these functions to make sure that they work.

## Getting Started

Before we can start writing tests, we need to do a little bit of set up. We will have to write a little bit of what is often referred to as 'boilerplate' code - code which has to be included in many places with very little modification. All of our Python test files will be written in more or less the same way.

The first thing that we have to do is import `unittest`, Python's built-in testing module, into our test file. We will also need to import the code that we want to test, in this case we want to test the calculator functions so we will import those too.

```python
# tests/calculator_test.py

import unittest
from src.calculator import add, divide, multiply, subtract
```

Now that we have everything that we're going to need, we can define our test class. According to convention, this should be named Test followed by the name of the module (or unit) that we're testing. In this case, our test class will be called `TestCalculator`, as we're testing the calculator module. Our test class should also inherit from `unittest.TestCase`. This will provide our test class with the functionality that we need in order to test our code.

```python
# tests/calculator_test.py

import unittest
from src.calculator import add, divide, multiply, divide

class TestCalculator(unittest.TestCase): # NEW
    pass                                 # NEW
```

Now that our test class is set up, we can write our first test. To write a test, we define a method on the test class. When we come to run our test file with `unittest`, it will automatically run all of these methods as tests.

## Writing a Test

We'll begin by writing a test for the `add` function. By convention we should begin the name of our tests with `test_` followed by name of the behaviour that we're testing. We will call this test `test_add`.

```python
# tests/calculator_test.py

class TestCalculator(unittest.TestCase):
    def test_add(self): # NEW
        pass            # NEW
```

Now that we have defined our test, let's think about how we can test that the `add` function works.

If we were to invoke our `add` function, providing the arguments `2` and `3`. What would we expect to get back? Assuming the add function works as expected, we should expect to get `5` back. When writing a test we provide a hard-coded "expected" value. The result that we expect to see. We can then call the function and compare our expected value against the value that we actually got back. If the expected value and the actual value are the same, then we can safely assume that our code is working.

`unittest` provides us with a method called `assertEqual`, which does exactly that. `assertEqual` takes two arguments, the expected value and the actual result, and compares them. If they're the same then the test passes. If they aren't the same then the test will fail and `unittest` will tell us what the expected and actual values were, so that we can begin to debug our code.

```python
# tests/calculator_test.py

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3)) # NEW
```

The function that we're testing here is very simple. It takes two numbers and adds them together. When we're testing more complex functionality, our tests may also become more complex. There are lots of different methodologies that help us structure tests. One of the most important is "the three As of testing".

### The Three As of Testing

The three As of testing are:

1. Arrange
2. Act
3. Assert

First, we arrange our test environment. This means that performing any setup that may be required in order to test the functionality. You may need to instantiate objects for the test, or ensure that an object is in a certain state during the test. You would need to add some items to an array if you were testing a sort function, for example. Simple tests will not require any arrangement, but others will.

Secondly, we perform the action that we are trying to test. In this case we called the `add` function inline, passing its return value directly to `assertEqual`, but you may see the same test written as follows:

```python
# Example

def test_add(self):
    expected = 5
    actual = add(2, 3)
    self.assertEqual(expected, actual)
```

Lastly, we make our assertion. Is the expected value the same as the value that actually came back?

## Running our Tests

We've written a test, now how do we run it? We'll run it from run_tests.py, so we need to pop a little bit more boilerplate code in there. We will need to import `unittest`, so that the file is able to run the tests properly, and we'll need to import our test class so that we can run it. If we were testing multiple modules or classes, we would have a separate test class for each.

```python
# run_tests.py

import unittest                                  # NEW
from tests.calculator_test import TestCalculator # NEW
```

Now we just need to tell Python to have `unittest` do its thing with our test classes.

```python
# run_tests.py

import unittest
from tests.calculator_test import TestCalculator

if __name__ == "__main__": # NEW
    unittest.main()        # NEW
```

> It's important to note that we're using `unittest.main()`, not the generic `main()` here.

Now we should be able to run run_tests.py and see that our test passes. We can rest assure that our code works as we expected it to.

```sh
# Terminal

python3 run_tests.py

# > Ran 1 tests in x.xs
# > OK
```

Excellent, our code works. Next we'll write a test for the subtract function. When we call the `subtract` function providing 10 and 7 as arguments, we expect to get back 3.

## Adding Additional Tests

```python
# tests/calculator_test.py

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(5, add(2, 3))

    def test_subtract(self):
        self.assertEqual(3, subtract(10, 7))
```

We don't need to add anything to run_tests.py. It will automatically run all of the tests in this class. We can simply run the file again and `unittest` will take care of the rest.

```sh
# Terminal

python3 run_tests.py

# > Ran 2 tests in x.xs
# > OK
```

### Task

Write tests for the remaining calculator methods - `divide` and `multiply`.

<details>
<summary>Solution</summary>

```python
def test_divide(self):
    self.assertEqual(2, divide(10, 5))

def test_multiply(self):
    self.assertEqual(10, multiply(5, 2))
```
</details>
