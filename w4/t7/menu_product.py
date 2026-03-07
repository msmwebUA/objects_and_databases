from product import Product
from db_conn import DB_CONN

class MenuProduct:

  def askChoice(self) -> int:
    choice = -1
    feed = input("Your choice: ").strip()
    if feed.isdigit():
      choice = int(feed)
    return choice

  def showOptions(self) -> None:
    print("Options:")
    print("1 - Add product")
    print("2 - Show products")
    print("0 - Exit")
    return None

  def run(self) -> None:
    while True:
      self.showOptions()
      choice = self.askChoice()
      if choice == 0:
        DB_CONN.close()
        break
      elif choice == 1:
        self.addProduct()
      elif choice == 2:
        self.showProduct()
      else:
        print("Unknown option, try again.")
      print()
    print("Program ending.")
    return None

  def addProduct(self) -> None:
    product_obj = Product.createProduct()
    print("Adding product...")
    product_obj.insertDB()
    print("Product added!")

  def showProduct(self) -> None:
    products = Product.queryProducts()
    print("No., Manufacturer, Brand, Cost, Price")
    counter = 1 # use counter for list of products, ! Product class has no id property
    for product in products:
      print(f"{counter}, {product.manufacturer}, {product.brand}, {product.cost}, {product.price}")
      counter += 1