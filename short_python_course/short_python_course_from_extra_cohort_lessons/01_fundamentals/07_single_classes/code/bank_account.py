class BankAccount:

  def __init__(self,name,value,type):
    self.name = name
    self.type = type
    self.value = value

  def get_name(self):
    return self.name

  def get_type(self):
    return self.type

  def get_value(self):
    return self.value

  def set_name(self, name):
    self.name = name

  def set_type(self, type):
    self.type = type

  def set_value(self, value):
    self.value = value
    
  def pay_in(self,value):
    self.value += value

  def pay_monthly_fee(self):
   if (self.type == 'personal'):
      self.value -= 10 
   elif(self.type == 'business'):
    self.value -= 50 


