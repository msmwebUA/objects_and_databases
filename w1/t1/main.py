from person import Person

class Main:
  def __init__(self) -> None:
    print("Program starting.")
    print("Initializing persons...")
    person1 = Person("Jane", "Morgan")
    person2 = Person("John", "Doe")
    print("Persons initialized, names below.")
    person1.fullname()
    person2.fullname()
    print("Program ending.")
    return None

if __name__ == "__main__":
  app = Main()