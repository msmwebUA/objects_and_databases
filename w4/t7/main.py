from menu_product import MenuProduct
from db_conn import DB_CONN

class Main():
  def __init__ (self) -> None:
    print("Program starting.")
    menu = MenuProduct()
    menu.run()
    return None

if __name__ == "__main__":
  app = Main()