## Composition

## Learning Objectives

- Be able to describe composition
- Understand why to favour composition over inheritance

# Intro

When we looked at inheritance when creating an object we were thinking about what an object __IS__ e.g. a `Car` __IS_A__ `Vehicle. 

As well as thinking about what something __IS__, we can also think about what something __HAS__ e.g. a car __HAS__ an engine, a car __HAS__ a gearbox. So our car is made up of, or ***COMPOSED*** of other objects, each with their own state and behaviour.

> maybe draw a class diagram of the following on the board
> maybe also show the code but don't get the class to code along

```python
#engine.py

class Engine:

    def start(self):
        return "Vrrrmmm!"
```

```python
# gearbox.py

class Gearbox:
    def __init__(self, type, number_of_gears):
        self.type = type
        self.number_of_gears = number_of_gears
        self.current_gear = "N"

    def change_gear(self, gear):
        self.current_gear = gear

```

```python
#car.py

class Car:
    def __init__(self, make, model, engine, gearbox):
        self.make = make
        self.model = model
        self.engine = engine
        self.gearbox = gearbox
```

### Composition and Behaviours

When we are thinking about what a Car does, i.e. its behaviour, we can think about what it HAS to carry out that behaviour i.e. an Engine, rather than what it IS that gives us that behaviour e.g. a `drive` method in a `Vehicle` superclass.

So in our `Car` example, if we want the car to accelerate we can ask ourselves what does a `Car` have that it would use to start? - an `Engine`. So for a car to start it could call the `start` method on it's engine object.

```python
#car.py

class Car:
    def __init__(self, make, model, engine, gearbox):
        self.make = make
        self.model = model
        self.engine = engine
        self.gearbox = gearbox

    def start(self):
        return self.engine.start()
```

> Question: how would the car change gear?
> Answer:

```python
#car.py

class Car:

  # AS BEFORE 

  def change_gear(self, gear):  # ADDED
      self.gearbox.change_gear(gear)
```

So rather than inheriting from a superclass to get the functionality we need, we compose our object from other objects. We've been doing this already without actually calling it Composition

> think of an example from previous lessons - the band?

Using composition means that we can change the behaviour of a car, simply by swapping one component for another. For example, we can change the behaviour of the `Car`'s `start` method simply by swqpping a `Car`'s engine for a different engine with a different `start` method. We could do this using inheritance by overriding the method in the parent class, but that is static, and so cannot change. By using composition we can swap the engine in/out we can do this while our program is running, so is much more flexible.

So, anything that can be implemented using inheritance can also be implemented using composition. So what should we use - inheritance or composition?

### Inheritance OR Composition?

In programming there is the idea have the saying favour composition over inheritance. We should compose our classes from other classes that implement the behaviours we need. 

If we want objects of different classes to share the same behaviour then we can do this using composition. For example, if we want both a `Car` and a `Motorbike` to be able to start, then we can give them both an `Engine` which has it's own `start` method:

```python
#car.py

class Car:
    def __init__(self, make, model, engine, gearbox):
        self.make = make
        self.model = model
        self.engine = engine
        self.gearbox = gearbox

    def start(self):
        return self.engine.start()
```

```python
#motorbike.py

class Motorbike:

    def __init__(self, make, model, engine):
        self.make = make
        self.model = model
        self.engine = engine

    def start(self):
        return self.engine.start()
```

```python
engine = Engine()
gearbox = Gearbox("manual", 5)

car = Car("Ford", "Escort", engine, gearbox)
motorbike = Motorbike("Yamaha", "FZR1000", engine)

car.start()
motorbike.start()
```

Inheritance can be useful and should not be disregarded totally. If the relationship between two classes is an __IS_A__ relationship, then use inheritance. If the relationship is a __HAS_A__ relationship, then use composition.

### Quiz 

What kind of relationship do you think each of these is?

- Computer & CPU.
<details>
<summary>Answer</summary>
__HAS_A__
</details>

- Circle & Shape.
<details>
<summary>Answer</summary>
__IS_A__
</details>

- Triangle & Sides
<details>
<summary>Answer</summary>
__HAS_A__
</details>

- Laptop & Computer.
<details>
<summary>Answer</summary>
__IS_A__
</details>

- Chair & Legs
<details>
<summary>Answer</summary>
__HAS_A__
</details>

## Recap

- Composition is where an object is made up of one or more other objects.
- Composition is usually favoured over inheritance.