from car import Car

COLORS = ["red", "green", "blue"]

class Main:
  def __init__(self) -> None:
    print("Program starting.")
    print("Initializing three car objects.")
    cars: list = []
    for color in COLORS:
      cars.append(Car(color))
    print("Car objects initialized.")
    # start all cars in list
    for car, seq in zip(cars, ("first", "second", "third")):
        print(f"Starting the {seq} car object.")
        car.start()
    # try to start last car again
    print(f"Starting the third car object.")
    cars[2].start()
    # finish
    print("Program ending.")
    return None

if __name__ == "__main__":
  app = Main()