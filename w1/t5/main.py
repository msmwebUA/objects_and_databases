from coin_acceptor import CoinAcceptor

COIN_ACCEPTOR = CoinAcceptor()

class Main:
  def __init__(self) -> None:
    print("Program starting.")
    print("Welcome to coin acceptor program.")
    print("Insert new coin by typing it's value (0 returns the money, -1 exits the program)")
    while True:
      print()
      user_input = input("Insert coin(0 return, -1 exit): ").strip()
      if user_input == "-1":
        print("Exiting program.")
        break
      elif user_input == "0":
        print("Returning coins...")
        coins_returned = COIN_ACCEPTOR.returnCoins()
        print(f"{coins_returned[0]} coins with {coins_returned[1]}€ value returned.")
        getSaldo()
      else:
        print("Inserting...")
        COIN_ACCEPTOR.insertCoin(float(user_input))
        getSaldo()
    print("\nProgram ending.")
    return None

def getSaldo() -> None:
  saldo = COIN_ACCEPTOR.getAmount()
  print(f"Inserted coins - {saldo[0]}, value - {saldo[1]}€")
  return None

if __name__ == "__main__":
  app = Main()