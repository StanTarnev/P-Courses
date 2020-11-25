# Testing Recap

**Lesson Duration: 30 minutes**

### Learning Objectives

- Recap testing
- Know how to set up directories for testing
- Know how to write a test

## Recap

So we will be doing `unit testing`. Unit testing is a level of software testing where small individual components of code (often a method) are testing.

We do this by using the built in `unittest` module in Python.

Our unit tests are written in a separate file to our main code and usually saved in a separate directory.

So let's set up our directory structure for the lab.

## Setting up directories and files

```bash
# Terminal

mkdir pub_lab
mkdir pub_lab/src
mkdir pub_lab/tests
touch run_tests.py
```

To run our tests we'll run the `run_tests.py` file. But first let's add some code to his file.

```python

# run_tests.py

import unittest


if __name__ == '__main__':
    unittest.main()

```

Now let's save we have a Pub class that we need to test.

We'll create a file for the class and a file for the test.

```bash
touch src/pub.py
touch tests/pub_test.py
```

Let's add some initial boilerplate code to pub_test.py

```python
# tests/pub_test.py

import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    pass
```

And we'll import the `pub_test` file into our `run_tests.py`

```python
# run_tests.py

import unittest
from tests.pub_test import TestPub

if __name__ == '__main__':
    unittest.main()

```

Ok so now we should be good to run our `run_tests.py` file.

```bash
# Terminal

python run_tests.py

```

## Setup method

Remember to use a `setUp` method. For example:


```python
# tests/pub_test.py

import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self): # NEW
      self.pub = Pub("The Prancing Pony", 100.00) # NEW

```

Let's add our first test. We can expect it to fail. Our job then is to get it to pass!

```python
# tests/pub_test.py

import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):

    def setUp(self):
      self.pub = Pub("The Prancing Pony", 100.00)

    def test_pub_has_name(self): # NEW
        self.assertEqual("The Prancing Pony", self.pub.name) # NEW

```

Run the tests again!

```bash
# Terminal

python run_tests.py

```


## Conclusion

That's us set up a basic structure for our project. For clarity, it's conventional to have one test file for each class. This is not a strict rule but it makes sense if it's possible.
