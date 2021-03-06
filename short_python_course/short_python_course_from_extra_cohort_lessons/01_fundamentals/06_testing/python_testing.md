# Testing

We just wrote a nice greet method.

```
def greet(name, time_of_day):
    return "Good " + time_of_day + ", " + name.capitalize()

if __name__ == "__main__":
    print(greet("john", "morning"))
```

When we write our code, we want to make sure it works. It sounds obvious but let's have a think about it. We can craft better code if it's tested. How do we test?

There are many approaches to testing our code but the principles are the same. What we want to do is write code which asserts an expectation and returns true or false on the outcome. Or pass or fail!

### Test Driven Development

One way of programming is to write the test first and make it fail, and then write the code to make it pass.  

We are going to recreate our greet method in this way.

TDD has been shown to result in:
- Fewer bugs
- A more maintainable codebase
- Code that is "documented" - we can tell from the tests how to use the code!
- More modular code

We would  usually write our tests in a separate file, 

```
touch my_functions_spec.py
```

We're going to run this spec file manually,to make sure that our function does what we think it's going to do.

Let's open it up and get started.

```
import unittest
from my_functions import *

class FunctionsPracticeTest(unittest.TestCase):
    def test_greet(self):
        greeting = greet("john", "morning")
        self.assertEqual(greeting, "Good morning, John");

if __name__ == "__main__":
    unittest.main()
```

We can run this in terminal:

```
python specs/my_functions_spec.py
```

Python doesn't know about this function, so we get a `NameError:name 'greet' is not defined`.

### Fail, try again, fail better.

Let's get closer to passing test in small iterations:

```
    def greet(name, time_of_day)
        return None
```

And now let's make it pass

```
    def greet(name, time_of_day)
        return "Good " + time_of_day + ", " + name
```

We can now write another test to make sure that our name is capitalized.

```
def test_capitalizes_name(self):
    greeting = greet("john", "morning")
    self.assertEqual(greeting, "Good morning, John")
```

And let's make this one pass:

```
    def greet(name, time_of_day)
        return "Good " + time_of_day + ", " + name.capitalize()
```

We produced the same functionality we had earlier, using test driven development.  We arrived at the same situation but this time with test coverage for basic usage and capitalisation.

### Good/bad method names

It's always useful to use function names that say what the function does - use snake case.


### More functions

Let's create an add function. We want to test drive our code in our spec. What do we need to do step by step:

1. setup test
2. decide a good method name for add? `add` is probably good!
3. invoke our function that we haven't created
4. use the self.assertEqual method which takes two arguments
  - the called method
  - the expected result

```
def test_add(self):
    result = add(2, 3)
    self.assertEqual(result, 5)
```

If we run this spec. We should get an NameError for add(). This is handy, it's telling us what to do! We need to go and define a method add().

```
def add():
    return None
```

OK! Now we're seeing `TypeError: add() takes 0 positional arguments but 2 were given`. 

This is telling us that we've given it two arguments when we've called it, but the function definition doesn't expect any.

Let's fix that.

```
def add(a, b):
    return None
```

What are we seeing when we run the test now? We're seeing that None != 5. (None doesn't equal five.) So everything else seems to be working, but we're not getting the expected result. One final change should let our code work as expected.

```
def add(a, b):
    return a + b
```

[i]: Optional task, test drive a subtract function.