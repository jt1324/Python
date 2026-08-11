from rich import print
import hashlib
import pwinput

class BankAccount:
  def __init__(self, id, name, balance=0, password=None):
    self._id = id
    self._owner = name
    self.__balance = balance
    self.__hash = ""
    if password is None:
      password = pwinput.pwinput(prompt="Enter a password: ", mask="*")
    self.__hash = hashlib.sha256(password.encode()).hexdigest()
    print(f"Account {self._id} created succesfully. Ballance £{self.__balance:,.2f}.")

  def __str__(self):
    return f"The account {self._id} from {self._owner} has £{self.__balance:,.2f} of balance."

  def depo(self, amount):
    self.__balance += amount
    print(f"Deposit of £{amount:,.2f} confirmed to account {self._id}.")

  def withd(self, amount, password=None):
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

  def password_check(self, password):
    if self.__hash == hashlib.sha256(password.encode()).hexdigest():
      print("Password correct")
      return True
    else:
      print("Password incorrect")
      return False

  def ask_password(self):
    return pwinput.pwinput(prompt="Enter a password: ", mask="*")
