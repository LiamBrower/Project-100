class ATM(object):
  """
    blueprint for atm
  """

  def __init__(self, model, color, company, cash_limit):
    self.model = model
    self.company = company
    self.color = color
    self.speed_limit = cash_limit

  def start(self):
    print("started")

  def stop(self):
    print("stopped")

  def dispense(self):
    print("dispensing...")
    "dispenser funcionality here"

  def chang_amount(self, gear_type):
    print("amount changed")
    " amount changing related functionality here"

atm = ATM("5.3.16", "green", "private_banker", 10,000)

print(atm.start())