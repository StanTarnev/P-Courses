# Python Classes - Part 2

## Getters

Normally in order to access properties, we need to create "getter" methods. This allows us to give people access to the propertiesand retrieve the value. Let's add a getter for the name.

```Python
# bank_account.py
def get_holder_name(self):
  return self.holder_name
```

Now our test will pass, since we have allowed access to our object's name. Let's do the same for a bank account's amount and type:

> [Task:] Write getters for the amount and the type of account, with tests first.

```Python
# bank_account_spec.py
def test_account_amount(self):
  account = BankAccount('john', 5000, 'business')
  self.assertEqual(5000, account.get_amount)

def test_account_type(self):
  account = BankAccount('john', 5000, 'business')
  self.assertEqual('business', account.get_type)
```

```Python
# bank_account.py
def get_amount(self):
  return self.amount

def get_type(self):
  return self.type
```

## Setters

Equally, we can write methods to set the value of our properties. We call these "setters". Let's add a setter.

```Python
# bank_account_spec.py
def test_set_account_name(self):
  account = BankAccount('john', 5000, 'business')
  account.set_holder_name('Darren')
  self.assertEqual('Darren',account.get_holder_name)
```

If we run this, we will get a "No method" error since we have not allowed access to set the value of the name. We can read it, but we can't set it. Let's sort that.

```Python 
# bank_account.py
def set_holder_name(self, name):
  self.holder_name = name
```

And we can write setters for the account amount and type:

> [Task:] Make setters for the value and type.

```Python

#bank_account_spec.py
def test_set_account_amount(self):
  account = BankAccount('john', 5000, 'business')
  account.set_amount(10000)
  self.assertEqual(10000,account.get_amount)

def test_set_account_type(self):
  account = BankAccount('john', 5000, 'business')
  account.set_type('personal')
  self.assertEqual('personal',account.get_type)
```

```Python
# bank_account.py
def set_amount(self, value):
  self.amount = value

def set_type(self, type):
  self.type = type
```


## Further Behaviour - not a setter

Let's define some further behaviour on the BankAccount, where we can update the value of the account.

```Python
# bank_account_spec.py
def test_pay_into_account(self):
  account = BankAccount('john', 5000, 'business')
  account.pay_in(1000)
  self.assertEqual(6000, account.get_amount)
```

If we run this, the test will fail and say it can't find the method pay_in. Which is correct, we need to go and add this to our class.

```Python
# bank_account.py
def pay_in(self, value):
  self.amount += value
```

This is not a setter or a getter, it's not simply updating the value or retrieving the value. It's modifying it with some logic.

## Conditional state

We sometimes want instances to behave slightly differently depending on their state (instance variables). Let's make a little pay monthly method, which subtracts 50 off the value of the account.

> [Task:] Make a pay_monthly_fee method, which reduces the value of the account by 50. Write the test first.

```Python
# bank_account_spec.py
def test_monthly_fee(self):
  account = BankAccount('john', 5000, 'business')
  account.pay_monthly_fee()
  self.assertEqual(4950, account.get_amount)
```

```Python
# bank_account.py
def pay_monthly_fee(self):
  self.amount -= 50
```

Our bank account currently isn't very fair, since personal users pay the same fee as a business user. Change the monthly fee method to deduct only 10 for a personal account, and 50 for a business account. You will need to update the tests.

>[Task:] Take a few minutes to do this

```Python
# bank_account_spec.py
def test_monthly_fee_business(self):
  account = BankAccount('john', 5000, 'business')
  account.pay_monthly_fee()
  self.assertEqual(4950, account.get_amount)


def test_monthly_fee_personal(self):
  account = BankAccount('darren', 5000, 'personal')
  account.pay_monthly_fee()
  self.assertEqual(4990, account.get_amount)

```

```Python
# bank_account.py
def pay_monthly_fee(self):
  if(self.type == 'personal'):
    self.amount -= 10
  elif(self.type == 'business'):
    self.amount -= 50
```

```Python
# bank_account.py
# Alternative solution
def pay_monthly_fee(self):
  charges = {
    'business': 50,
    'personal': 10
  }
  self.amount -= charges[self.type]
```
