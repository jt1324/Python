class BankAccount:
  """
  Docstring for BankAccount
  Create a bank account and allow it to make withdraws and deposits
  """

  def __init__(self, id, name, balance = 0):
    self.id = id
    self.owner = name
    self.balance = balance
    print (f"Account {self.id} created succesfully. Ballance £{self.balance:,.2f}.")

  def __str__(self):
    return f"The account {self.id} from {self.owner} has £{self.balance:,.2f} of balance."

  def depo(self, amount):
    self.balance += amount
    print (f"Deposit of £{amount:,.2f} confirmed to account {self.id}.")
  
  def withd(self, amount):
    if amount > self.balance:
      print(f'Insufficient balance for this withdrwal. Your balnace is £{self.balance:,.2f}.')
    else:
      self.balance -= amount
      print (f"Withdraw of £{amount:,.2f} authorised from account {self.id}.")


a1 = BankAccount(112, 'Jean', 3000)
a1.depo(1500)
a1.withd(5000)
print(a1)
# print(a1.__doc__)