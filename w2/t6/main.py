from menu import Menu
from soda_bottle import SodaBottle

class Main:
  def __init__ (self) -> None:
    print("Program starting.")
    menu = Menu()
    menu.loadBottles()
    menu.runMenu()
    return None

if __name__ == "__main__":
  app = Main()