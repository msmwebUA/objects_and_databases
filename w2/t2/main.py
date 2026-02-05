from soda_bottle import SodaBottle

class Main:
  def __init__ (self) -> None:
    print("Program starting.")
    fname = input("Insert filename: ").strip()
    with open(fname, encoding="UTF-8") as f:
      row = f.readline().strip()
    print(f'Deserializing "{row}"')
    bottle = SodaBottle.deserialize(row)
    print(f"Looks like {bottle.volume} litre {bottle.brand} bottle.")
    print("Program ending.")
    return None

if __name__ == "__main__":
  app = Main()