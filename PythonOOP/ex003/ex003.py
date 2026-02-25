class BankAccount:
  """
  Docstring for BankAccount
  Create a bank account and allow it to make withdraws and deposits
  """

  def __init__(self, id, name, balance = 0):
    self.id = id
    self.owner = name
    self.balance = balance

  def __str__(self):
    return f"The account {self.id} from {self.owner} has £{self.balance:,.2f} of balance."




a1 = BankAccount(112, 'Jean', 3000)
print(a1)