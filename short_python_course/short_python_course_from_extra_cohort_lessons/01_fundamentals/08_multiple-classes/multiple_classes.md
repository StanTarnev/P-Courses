# Multiple Classes

Well done! We have become object orientated programmers, by creating a class and instantiating objects using it.

Object orientated programming becomes really powerful when an object uses an other object to help it in a task.

Enough theory, let's look at an example.

## Delegating To Other objects

Let's look at the situation of a wizard that casts a spell using a wand. And let's say that the spell's strength depends on the wand's wood type and it's core.

First, we want to create tests for our Wizards.

```bash
# terminal

mkdir multiple_classes
cd multiple_classes
mkdir specs
touch specs/wizard_specs.py
```

Then open it up in your text editor!

```python
# specs/wizard_specs.py

import unittest
import sys
sys.path.append(".")
sys.path.append("..")

from wizard import *

class TestWizard(unittest.TestCase):
    def setUp(self):
        self.ron = Wizard("Ron Weasley", "oak", "unicorn hair")

    def test_wizard_name(self):
        self.assertEqual(self.ron.name, "Ron Weasley")

if __name__ == '__main__':
    unittest.main()
```

Great! The first thing we want to test is if we can create a wizard, and then access his/her name. Let's do it!

```bash
#terminal

touch wizard.rb
```

```python
class Wizard:
    def __init__(self, name, wand_wood, wand_core):
        self.name = name
        self.wand_wood = wand_wood
        self.wand_core = wand_core
```

Our test should pass no problem!

Wizards are no wizards without being able to cast spells. Let's add the ability of spellcasting to our wizard class!

Firstly, we write our test:

```python
# wizard_specs.py
def test_can_cast_spell(self):
    self.assertEqual(self.ron.cast_spell("stupor"), "stupor")
```

Then we write the method to pass the test!

```python
# wizard.py
def cast_spell(self, spell):
    return spell
```

Boom! Job's done. But then again, this is not really interactive. Let's do something with the wood type/core!

First, the test:

```python
def setUp(self):
    self.harry = Wizard("Harry Potter", "holly", "phoenix feather")

def test_can_cast_stronger_spell(self):
    self.assertEqual(self.harry.cast_spell("expecto patronum"), "EXPECTO PATRONUM")
```

```python
def cast_spell(self, spell):
    if(self.wand_wood == "holly" and self.wand_core == "phoenix feather"):
        return spell.upper()
    else:
        return spell
```

Great!

Wait...something is not quite right. What if I want to give Harry a new wand? Do I have to recreate him from scratch? This is not really clean... And is it really the wizard's responsibility to know about the wand's wood and core?

Let's delegate the job of knowing wand cores to an appropriate class - let's create a wand class!

```bash
touch wand.py
touch specs/wand_spec.py
```

```python
# wand_specs.py
import unittest
import sys
sys.path.append(".")
sys.path.append("..")

from wand import *

class TestWand(unittest.TestCase):
    def setUp(self):
        self.wand = Wand("holly", "phoenix feather")

    def test_wand_wood(self):
        self.assertEqual(self.wand.wood, "holly")

    def test_wand_core(self):
        self.assertEqual(self.wand.core, "phoenix feather")

if __name__ == '__main__':
    unittest.main()
```

And let's make our tests pass!

```python
class Wand:
    def __init__(self, wood, core):
        self.wood = wood
        self.core = core
```

Excellent!

Now here comes the magical part: From now on, we can instantiate a wand, and instead of the wizard being responsible for having a wand wood/core, the wand object can handle all this for us! Let's go back to our wizard.py, and refactor our code.

```python
class Wizard:
    def __init__(self, name, wand):
        self.name = name
        self.wand = wand

    def cast_spell(self, spell):
        return self.wand.cast_spell(spell)
```

Since it's the wand's job to keep track of the core/wood, we can give the responsibility of checking it to the wand class!

```python
# wand.py
def cast_spell(self, spell):
    if(self.wood == "holly" and self.core == "phoenix feather"):
        return spell.upper()
    else:
        return spell
```

Dang, but then our tests are failing! Let's rework them to suit them to the changes we made!

```python
def setUp(self):
    self.broken_wand = Wand("oak", "unicorn hair")
    self.elder_wand = Wand("holly", "phoenix feather")
    self.ron = Wizard("Ron Weasley", self.broken_wand)
    self.harry = Wizard("Harry Potter", self.elder_wand)
```

Did we have to change anything with our tests? No, we did not. Everything passes just as fine as before. The wizard here has _delegated_ the behaviour of their spell casting to the wand.

What object is responsible for what is one of the major challenges of object orientated programming.  There are thousands of books of this, and we enter the realm of Object Orientated Design.  For now I would not worry too much about the design and focus on getting things working.  Make it work, make it right, make it fast.

## Collection objects

> This bit is totally optional. There is a lab to cover this if the students are up to it.

We've already seen arrays and hashes. Objects whose role is to hold other objects.  Let's look at how we can use these to create our own collections.

```python
# coven_spec.py
import unittest
import sys
sys.path.append(".")
sys.path.append("..")

from wand import *
from wizard import *
from coven import *

class TestCoven(unittest.TestCase):
    def setUp(self):
        self.broken_wand = Wand("oak", "unicorn hair")
        self.elder_wand = Wand("holly", "phoenix feather")
        self.harry = Wizard("Harry Potter", self.elder_wand)
        self.ron = Wizard("Ron Weasley", self.broken_wand)

        self.coven = Coven([self.harry, self.ron])

    def test_coven_can_cast_spell(self):
        expected = ["STUPOR", "stupor"]
        self.assertEqual(self.coven.cast_spell("stupor"), expected)
```

```python
# coven.py
class Coven:
    def __init__(self, wizards):
        self.wizards = wizards

    def cast_spell(self, spell):
        mass_spell = []

        for wizard in self.wizards:
            mass_spell.append(wizard.cast_spell(spell))

        return mass_spell
```
