import unittest
import sys
sys.path.append(".")
sys.path.append("..")
from bank_account import *

class TestBankAccount(unittest.TestCase):
  def test_account_name(self):
   account = BankAccount('john', 5000, 'business')
   self.assertEqual('john',account.get_name())

  def test_account_value(self):
   account = BankAccount('john', 5000, 'business')
   self.assertEqual(5000,account.get_value())

  def test_account_type(self):
   account = BankAccount('john', 5000, 'business')
   self.assertEqual('business',account.get_type())

  def test_set_account_name(self):
    account = BankAccount('john', 5000, 'business')
    account.set_name('Valerie')
    self.assertEqual('Valerie',account.get_name())


  def test_set_account_value(self):
    account = BankAccount('john', 5000, 'business')
    account.set_value(10000) 
    self.assertEqual(10000,account.get_value())

  def test_set_account_type(self):
    account = BankAccount('john', 5000, 'business')
    account.set_type('personal') 
    self.assertEqual('personal',account.get_type())

  def test_pay_into_account(self):
   account = BankAccount('john', 5000, 'business')
   account.pay_in(1000)
   self.assertEqual(6000, account.get_value())

  def test_monthly_fee_business(self):
    account = BankAccount('john', 5000, 'business')
    account.pay_monthly_fee()
    self.assertEqual(4950, account.get_value())

  def test_monthly_fee_personal(self):
    account = BankAccount('darren', 5000, 'personal')
    account.pay_monthly_fee()
    self.assertEqual(4990, account.get_value())

if __name__ == "__main__":
    unittest.main()