# Inheritance

## Learning Objectives

- Be able to describe inheritance
- Implement superclass and subclass
- Know how to override methods
- Sharing a constructor

> Duration 2 hours

Sometimes we might have a bunch of classes that all share some behaviour. For example, a sparrow can fly, but so can a crow.

A car has wheels, but so does a motorbike - they also both help you travel somewhere, and both have an engine that can start.

How can we represent this in our code?

```bash
#terminal

touch car.py motorbike.py
mkdir specs
touch specs/car_spec.py specs/motorbike_spec.py

subl .
```

```python
# car_spec.py
import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from car import *

class TestCar(unittest.TestCase):
  def setUp(self):
    self.car = Car()

  def test_car_can_start_engine(self):
    self.assertEqual("Vrrmmm", self.car.start_engine())

if __name__ == "__main__":
  unittest.main()
```

```python
# car.py
class Car:
  def start_engine(self):
    return "Vrrmmm"
```

Now if we want to make a motorbike that also starts its engine what do we do? The simplest solution is that we can copy and paste the code.

```python
# motorbike_spec.py

import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from motorbike import *

class TestMotorbike(unittest.TestCase):
  def setUp(self):
    self.motorbike = Motorbike()

  def test_motorbike_can_start_engine(self):
    self.assertEqual("Vrrmmm", self.motorbike.start_engine())

if __name__ == "__main__":
  unittest.main()
```

```python
# motorbike.py
class Motorbike:
  def start_engine(self):
    return "Vrrmmm"
```

This is dirty. We want to be able to reuse our code.

If we change this method we need to alter it in two places. We can move this to a "super class" where the behaviour can be shared among the two "sub classes".

```bash
# terminal

touch vehicle.py
```

```python
# vehicle.py
class Vehicle:
  def start_engine(self)
    return "Vrrmmm"
```

```python
# vehicle_spec.py
import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from vehicle import *

class TestVehicle(unittest.TestCase):
  def setUp(self):
    self.vehicle = Vehicle()

  def test_vehicle_can_start_engine(self):
    self.assertEqual("Vrrmmm", self.vehicle.start_engine())

if __name__ == "__main__":
  unittest.main()
```

Now have Car and Motorbike inherit from Vehicle by passing into class and removing their start_engine() functions.

```python
# car.py
from vehicle import *
class Car(Vehicle):
  pass
```

```python
# motorbike.py
class Motorbike(Vehicle):
  pass
```

Our tests still pass. This is as if the two classes are joined together - the behaviour is passed down to the subclass. This is called "inheriting" properties or behaviours.

## Overriding

If we declare a method with the same name in a subclass that is shared with a parent, we override it. Python first looks to the class, and then the super class.  Let's change the motorbike so it has specific behaviour.

```python
# motorbike_spec.py

class MotorbikeTest(unittest.TestCase)
	def setUp(self)
    self.motorbike = Motorbike()

  def test_motorbike_can_start_engine(self):
    self.assertEqual("Vrrmmm (I'm a motorbike), HELL YEAH!", self.motorbike.start_engine())

if __name__ == "__main__":
  unittest.main()
```

```python
# motorbike.py
from vehicle import *
class Motorbike:
	def start_engine(self):
    return "Vrrmmm (I'm a motorbike), HELL YEAH!"
```

##`super`
What if wanted our motorbike to do something unique and to also do its parent behaviour.  Enter `super`.

`super` calls its parent (super) class method.

```python
# motorbike.py
from vehicle import *
class Motorbike(Vehicle):
  def start_engine(self):
    vehicle_start = Vehicle.start_engine(self)
    return "{vehicle_start} (I'm a motorbike), HELL YEAH!"
```

## Shared Constructor

Note that if we add a constructor to Vehicle, all of the derived classes share it.

```python
# vehicle.py

def __init__(self):
  self.number_of_wheels = 4

def get_number_of_wheels(self):
  return self.number_of_wheels
```

```python
# vehicle_spec.py

def test_vehicle_has_number_of_wheels(self):
  self.assertEqual(4, self.vehicle.get_number_of_wheels())
```

```python
# car_spec.py

def test_car_has_four_weels(self):
	self.assertEqual(4, self.car.get_number_of_wheels())
```

If we added a parameter to the constructor, all of our vehicle classes would have to use it.

```python
# vehicle.py

def __init__(self, number_of_wheels):
  self.number_of_wheels = number_of_wheels
```

```python
# vehicle_spec.py

def setup():
  self.svehicle = Vehicle(4)
```

Now if we want to set one of our subclasses to have that property as a constant value, e.g. so we don't have to keep on passing in that a car has four wheels, we can call super() on the intialize method and pass in the value.

```python
# car.py

def __init__(self):
  Vehicle.__init__(4)
```

We can do the same for our motorbike so it always has two wheels.

If we want to also pass additional parameters to the constructor, we can do this - we can override initialize and also call super to set the wheels.

```python
# car.py

def __init__(self, model):
  Vehicle.__init__(self, 4)
  self.model = model

def get_model(self):
  return self.model
```

```python
# car_spec.py

def setUp(self):
  self.car = Car("Ferrari")

def test_car_has_model(self):
  self.assertEqual("Ferrari", self.car.get_model())
```


> [Task:] Make your own mini chain of inheritance: Make a Person class.  A person should have a first name and last name and a talk method which says its name.  Make a Medic class which inherits from Person, and also has a heal method.  Make a Agent class that talks like an agent.  "The names Bond, James Bond".

# Finally..

This inheritance stuff seems pretty useful. However if we use it too much it can sometimes be limiting, or make us write our code in a convoluted way. For example, imagine we want to make a Bicycle class. Surely this should inherit from Vehicle - it does transport people around, and it does have wheels. However it doesn't have an engine, so inheriting a start_engine method is a bit of a problem.. what are some solutions?

- Overwrite the start_engine to just return 'I don't have an engine'
- Remove start_engine from vehicle and put it back on Car and Motorbike
- Add another layer of inheritance to have 'EnginedVehicles' and 'HumanPoweredVehicles'

... all of these are a bit nasty. This is where we come onto composition as an alternative way of structuring our programs.
