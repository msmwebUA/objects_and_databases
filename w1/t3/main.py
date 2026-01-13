from counter import Counter

OPTIONS = """
Options:
1) Add count
2) Get count
3) Zero count
0) Exit program"""

class Main:
  def __init__(self) -> None:
    print("Program starting.")
    print("Initializing counter...")
    counter = Counter()
    print("Counter initialized.")
    while True:
      print(OPTIONS)
      user_choice = input("Choice: ").strip()
      if user_choice == "0":
        break
      elif user_choice == "1":
        counter.addCount()
        print("Count increased")
      elif user_choice == "2":
        print(f"Current count '{counter.getCount()}'")
      elif user_choice == "3":
        counter.zeroCount()
        print("Count zeroed")
    print("\nProgram ending.")
    return None

if __name__ == "__main__":
  app = Main()