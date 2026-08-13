from rich import print
import hashlib
import pwinput

class BankAccount:
  def __init__(self, id:int, name:str = None, balance:float = 0, password:str = None):
    self._id = id
    self._name = name
    self.__balance = balance
    
    if password is None:
      password = self.ask_password()
    self.__hash = hashlib.sha256(password.encode()).hexdigest()
    print(f"Account {self._id} created succesfully. Ballance £{self.__balance:,.2f}.")

  def __str__(self):
    return f"The account {self._id} from {self._name} has £{self.__balance:,.2f} of balance."

  @property
  def name(self):
    return self._name

  @name.setter
  def name(self, value):
    ask_password = self.ask_password()
    if self.password_check(ask_password):
      self._name = value
      print(f"Name changed to {value}")
    else:
      print("Invalid password")

  def depo(self, amount):
    self.__balance += amount
    print(f"Deposit of £{amount:,.2f} confirmed to account {self._id}.")

  def withd(self, amount:float, password:str = None):
    amount = abs(amount)
    if password is None:
      password = self.ask_password()
    if self.password_check(password):
      if amount > self.__balance:
        print(f'Insufficient balance for this withdrwal. Your balnace is £{self.__balance:,.2f}.')
      else:
        self.__balance -= amount
        print(f"Withdraw of £{amount:,.2f} authorised from account {self._id}.")
    else:
      print("Invalid password")

  def password_check(self, password:str):
    if self.__hash == hashlib.sha256(password.encode()).hexdigest():
      print("Password correct")
      return True
    else:
      print("Password incorrect")
      return False

  def ask_password(self):
    
    while True:
      password = str(pwinput("Enter the password: ")).strip()
      if len(password) >=6:
        break
    
    return password
