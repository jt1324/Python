class BankAccount:
  """
  Docstring for BankAccount
  Create a bank account and allow it to make withdraws and deposits
  """

  def __init__(self, id, name, balance = 0):
    self.id = id
    self._owner = name
    self.__balance = balance
    print (f"Account {self.id} created succesfully. Ballance £{self.__balance:,.2f}.")

  def __str__(self):
    # return f"The account {self.id} from {self._owner} has £{self.__balance:,.2f} of balance."
    return f"Account current status: {self.__dict__}"

  def depo(self, amount):
    if amount < 0:
      print("You can't add a negative amount")
    else:
      self.__balance += amount
      print (f"Deposit of £{amount:,.2f} confirmed to account {self.id}.")
  
  def withd(self, amount):
    if amount < 0:
      print("You can't withdraw a negative amount")
    else:
      if amount > self.__balance:
        print(f'Insufficient balance for this withdrwal. Your balnace is £{self.__balance:,.2f}.')
      else:
        self.__balance -= amount
        print (f"Withdraw of £{amount:,.2f} authorised from account {self.id}.")


# a1 = BankAccount(112, 'Jean', 3000)
# a1.depo(1500)
# a1.withd(5000)
# print(a1)
# print(a1.__doc__)