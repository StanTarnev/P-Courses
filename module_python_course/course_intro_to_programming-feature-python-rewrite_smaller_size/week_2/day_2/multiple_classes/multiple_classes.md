# Multiple Classes

**Duration: 90 minutes**

## Learning Objectives

- Use multiple classes together

### Introduction

So far, we have started our journey into Object Oriented Programming by writing single classes. But in the real world, things don't exist in isolation - they interact with each other.

We're going to investigate how we can develop our programs by making our classes interact with each other. We're going to model a pet shop, which interacts with customers and pets.

> Hand out start point

Our start point contains a `customer_test`, `pet_test`, `pet_shop_test` and `Pet` class.

### Managing a person/customer.

So let's start off with the next most simple type of class which would be our customer.

So we are going to create a Customer class.

Customers will have:

- name
- cash
- pets (List - starts off empty)

Customers should be able to

- add a pet
- add/remove cash

Let's start off by looking at the test file for customer.

```python
# customer_test.py

import unittest

from classes.customer import Customer
from classes.pet import Pet

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jack Jarvis", 1000)
        self.pet =  Pet("Blue", "cat", "British Shorthair", 500)

    
    def test_customer_has_name(self):
        self.assertEqual("Jack Jarvis", self.customer.name)

    def test_customer_has_cash(self):
        self.assertEqual(1000, self.customer.cash)

    # REST OF THE TESTS ARE COMMENTED OUT
```

When setting up a new customer we want them to have an empty list at the beginning. temptation is to pass in an empty list when we create the customer but this is actually bad practice. Think about it... every customer would be passed an empty list. This is a waste as it will always be the same. We will look at how we get around this shortly.

First we will create the customer class to get the tests passing.

```bash
# terminal
touch classes/customer.py
```

## Task

Create the customer class to get the tests passing. (Don't worry about the pets list just yet)

```python
# customer.py

class Customer:

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash

```

Cool our tests now pass.

Next let's deal with the customers pets.

As we said we want the customer to have an empty pets array when they are created. To do this we simply define a new instance variable in `__init__` and set it to be an empty list.

```python
# customer.py

class Customer:

    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.pets = []

```

Great now every time we new up a customer they will have an empty pets list.

In our test file we have a test which checks if the number of pets a customer has starts at 0. Let's unskip this test.

```python
# customer_test.py

# @unittest.skip("delete this line to run the test") DELETED
def test_pets_start_at_0(self):
    self.assertEqual(0, self.customer.pet_count())

```

Note that to test the number, it doesn't access the list directly, but calls a method `pet_count`

### Task

Write the `pet_count` method to get the test passing.

```python
# customer.py

def pet_count(self):
    return len(self.pets)
  
```

Great.

Next we probably want to be able to add a pet to the customer.

So that's fine as well. We just need a method to add a pet to the customers pet list.

Again, we have a test for this. We will use the `pet_count` method to check that this has worked.

```python
# customer_test.py

 #   @unittest.skip("delete this line to run the test") DELETED
    def test_can_add_pet(self):
        self.customer.add_pet(self.pet)
        self.assertEqual(1, self.customer.pet_count())
```

### Task

Write the code to get the test passing.

```python
# customer.py

def add_pet(self, pet):
    self.pets.append(pet)
```

Fantastic so now we are able to add a pet to our customer.

Now that our customer has an list of pet objects they can access the methods and properties of each pet.

Let's say, for example, that we wanted the customer to be able to return us the total cost of all their pets.

Again, we have a test for this which is currently skipped, so let's 'un-skip' it:

```python
# customer_test.py

# @unittest.skip("delete this line to run the test") DELETED
def test_can_get_total_pet_cost(self):
    self.customer.add_pet(self.pet)
    self.customer.add_pet(self.pet)
    self.customer.add_pet(self.pet)

    self.assertEqual(1500, self.customer.get_total_value_of_pets())
```

And now we will get that test passing.

```python
# customer.py

def get_total_value_of_pets(self):
    total = 0
    for pet in self.pets:
        total += pet.price
    return total

```

So now the customer can get the total value of all their pets.

## Pet Shop

Last thing to do now is to get the pet shop involved in all this.

The pet shop will be a place to store all the pets for sale.

So our pet shop will have:

- name
- pets (List that will be passed in.)
- pets_sold
- cash

And our pet shop will be able to:

- add pet
- remove pet
- sell pet to a customer.

This time instead of having an empty lsit we will pass in a pre-filled list of pets to the shop. But `pets_sold` will always start at 0 so we will set this in `__init__`.

Have a look at the pet_shop_test.

```python
# pet_shop_test.py
import unittest

from classes.pet_shop import PetShop
from classes.pet import Pet
from classes.customer import Customer

class TestPetShop(unittest.TestCase):
    def setUp(self):
        self.pet_1 =  Pet("Sir Percy", "cat", "British Shorthair", 500)
        self.pet_2 =  Pet("King Arthur", "dog", "Husky", 900)

        pets = [pet_1, pet_2]
        self.pet_shop = PetShop("Camelot of Pets", pets, 1000)

    def test_pet_shop_has_name(self):
        self.assertEqual("Camelot of Pets", self.pet_shop.name)

    @unittest.skip("delete this line to run the test")
    def test_pet_shop_case(self):
        self.assertEqual(1000, self.pet_shop.total_cash)

    @unittest.skip("delete this line to run the test")
    def test_pet_shop_pets_sold_starts_at_0(self):
        self.assertEqual(0, self.pet_shop.pets_sold)

    @unittest.skip("delete this line to run the test")
    def test_pet_shop_stock_count(self):
        self.assertEqual(2, self.pet_shop.stock_count())

    @unittest.skip("delete this line to run the test")
    def test_increase_pets_sold(self):
        self.pet_shop_increase_pets_sold()
        self.assertEqual(1, self.pet_shop.pets_sold)

    @unittest.skip("delete this line to run the test")
    def test_can_increase_total_cash(self):
        self.pet_shop.increase_total_cash(500)
        self.assertEqual(1500, self.pet_shop.total_cash)

    @unittest.skip("delete this line to run the test")
    def test_can_add_pet_to_stock(self):
        new_pet = Pet("Lancelot", "dog", "Basset Hound")
        self.pet_shop.add_pet(new_pet)
        self.assertEqual(3, self.pet_shop.stock_count())

    @unittest.skip("delete this line to run the test")
    def test_can_remove_pet_from_stock(self):
        self.pet_shop.remove(self.pet_1)
        self.assertEqual(1, self.pet_shop.stock_count())

    @unittest.skip("delete this line to run the test")
    def test_can_find_pet_by_name(self):
            pet = self.pet_shop.find_pet_by_name("Sir Percy")
            self.assertEqual("Sir Percy", pet.name)

    @unittest.skip("delete this line to run the test")
    def test_can_sell_pet_to_customer(self):
        customer = Customer("Jack Jarvis", 1000)
        self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
        self.assertEqual(1, customer.pet_count())
        self.assertEqual(1, self.pet_shop.stock_count())
        self.assertEqual(1, self.pet_shop.pets_sold)
        self.assertEqual(1500, self.pet_shop.total_cash)

```

### Task

Un-skip one test at a time and code the pet shop class to get all the tests up to, and including `test_can_find_pet_by_name` passing

(Remember that `PetShop` will have a `pets_sold` property that starts at 0)

```python
# pet_shop.py

class PetShop:
    def __init__(self, name, pets, total_cash):
        self.name = name
        self.pets = pets
        self.total_cash = total_cash
        self.pets_sold = 0

    def stock_count(self):
        return len(self.pets)

    def increase_pets_sold(self):
        self.pets_sold += 1

    def increase_total_cash(self, amount):
        self.total_cash += amount

    def add_pet(self, pet):
        self.pets.append(pet)

    def remove_pet(self, pet):
        self.pets.remove(pet)
```

### Selling a pet to a customer.

Lastly we will sell a pet to our customer.

So where will this happen?

We can either do this 2 ways. We can have a method in customer to buy pet or have a method in `PetShop` to sell to customer.

We are going to write a `buy_pet` method in the pet shop class.

Why?

Easy....Because it is the pet shop is the one selling the pet. So they should trigger the process. All the customer needs to know is the pet they want to buy.

We have a test for this which is currently skipped. 

```python
# pet_shop_test.py

#@unittest.skip("delete this line to run the test") DELETED
    def test_can_sell_pet_to_customer(self):
        customer = Customer("Jack Jarvis", 1000)
        self.pet_shop.sell_pet_to_customer("Sir Percy", customer)
        self.assertEqual(1, customer.pet_count())
        self.assertEqual(1, self.pet_shop.stock_count())
        self.assertEqual(1, self.pet_shop.pets_sold)
        self.assertEqual(1500, self.pet_shop.total_cash)
```

This is an example of an integration test. So when a customer buys a pet we want:

Customer's pet count to go up by 1
Shop's stock to go down
Shop's pets sold to go up.
Shop's `total_cash` to increase by price of pet.

To do this we will pass in the name of the pet and use the pet shop to find that pet.

In this test we set up a customer to buy the pet.

Next we pass the name of the pet and the customer to a `sell_pet_to_customer` method in pet shop.

Then we set up our asserts.

And now we can code the `sell_pet_to_customer` method in the pet shop.

The first thing this should do is find the pet to sell. (We won't worry about cases where the pet is not found just yet)

```python
# pet_shop.py

def sell_pet_to_customer(self, name, customer):
    pet = find_pet_by_name(name)

```

Now that we have found the pet we will add the pet to the customer.

To do this we will have the shop call a method in the customer to trigger this update.

Thankfully we have an 'add_pet' method available in the customer.

We can do this as we passed the customer into the `sell_pet_to_customer` method. We have access to all the things customers can do.

```ruby
# pet_shop.rb

def sell_pet_to_customer(self, name, customer):
    pet = self.find_pet_by_name(name)
    customer.add_pet(pet)
```

Next is to remove that pet from the stock

```ruby
# pet_shop.rb

def sell_pet_to_customer(self, name, customer):
    pet = self.find_pet_by_name(name)
    customer.add_pet(pet)
    self.remove_pet(pet)
```

And finally increase the pets sold and the total cash.

```ruby
# pet_shop.rb

def sell_pet_to_customer(self, name, customer):
    pet = self.find_pet_by_name(name)
    customer.add_pet(pet)
    self.remove_pet(pet)
    self.increase_pets_sold()
    self.increase_total_cash(pet.price)
```

### Conclusion

One way we can make objects interact is to add a list as an instance variable. But it doesn't have to be an list! An instance variable could be a single object, such as customers only having a single `Pet` property, for example.

In this case we're passing a full `Customer` object into the `sell_pet_to_customer` method in the `PetShop` so we can also call methods on the `Customer` object passed in.

For example, a car class might have an `engine` property. and to start the car, we might do `engine.start()`. This is a process called _composition_, and we'll look at it in more detail later on in the course.
