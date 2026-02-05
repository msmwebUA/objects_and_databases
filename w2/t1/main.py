from soda_bottle import SodaBottle

class Main:
  def __init__ (self) -> None:
    print("Program starting.")
    print("Constructing soda bottle.")
    brand = input("Insert brand: ").strip()
    volume = input("Insert volume: ").strip()
    bottle = SodaBottle(brand, volume)
    print("SodaBottle object created!")
    print("Serializing SodaBottle object.")
    print("Serialized sodabottle:")
    print(bottle.serialize)
    print("Program ending.")
    return None

if __name__ == "__main__":
  app = Main()