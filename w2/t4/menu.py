from soda_bottle import SodaBottle

class Menu:
  bottles: list = []

  def askChoice(self) -> int:
    while True:
      choice = -1
      feed = input("Your choice: ").strip()
      if feed.isdigit():
        choice = int(feed)
      return choice

  def addBottle(self) -> None:
    print("Creating soda bottle.")
    brand = input("Insert brand: ").strip()
    volume = input("Insert volume: ").strip()
    soda_bottle = SodaBottle(brand, volume)
    self.bottles.append(soda_bottle)
    return None

  def showBottle(self) -> None:
    print("#### Soda bottles ####")
    for bottle, index in zip(self.bottles, range(len(self.bottles))):
      print(f"Bottle {index + 1}:")
      print(f"  brand - {bottle.brand}")
      print(f"  volume - {bottle.volume}")
    print("#### Soda bottles ####")
    return None

  def saveBottle(self) -> None:
    print("'save' not implemented yet.")
    return None

  def runMenu(self) -> None:
    while True:
      print("Menu:")
      print("1 - Add bottle")
      print("2 - Show bottles")
      print("3 - Save bottle")
      print("0 - Exit")
      choice = self.askChoice()
      if choice == 0:
        print()
        break
      elif choice == 1:
        self.addBottle()
      elif choice == 2:
        self.showBottle()
      elif choice == 3:
        self.saveBottle()
      else:
        print("Unknown option, try again.")
      print()
    print("Exiting program.")
    print("Program ending.")
    return None
