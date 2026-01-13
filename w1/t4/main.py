from coin_acceptor import CoinAcceptor

OPTIONS = """1 - Insert coin
2 - Show coins
3 - Return coins
0 - Exit program"""

class Main:
  def __init__(self) -> None:
    print("Program starting.")
    coin_acceptor = CoinAcceptor()
    while True:
      print(OPTIONS)
      user_choice = input("Your choice: ").strip()
      if user_choice == "0":
        break
      elif user_choice == "1":
        coin_acceptor.insertCoin()
        print()
      elif user_choice == "2":
        print(f"Currently '{coin_acceptor.getAmount()}' coins in coin acceptor")
        print()
      elif user_choice == "3":
        coins_returned = coin_acceptor.returnCoins()
        print(f"Coin acceptor returned '{coins_returned}' coins.")
        print()
      else:
        print("Invalid option.")
    print("Program ending.")
    return None

if __name__ == "__main__":
  app = Main()