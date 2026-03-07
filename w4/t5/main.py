from db_conn import DB_CONN

PRODUCT_TABLE_CREATE = """
CREATE TABLE IF NOT EXISTS product (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  manufacturer VARCHAR(255) NOT NULL,
  brand VARCHAR(255) NOT NULL,
  cost REAL NOT NULL,
  price REAL NOT NULL
)"""

PRODUCT_TABLE_INSERT = """
INSERT INTO product (manufacturer, brand, cost, price) VALUES (:manufacturer, :brand, :cost, :price);
"""

class Main():
  def __init__ (self) -> None:
    print("Program starting.")
    print("Insert product details below:")
    manufacturer = input("- Insert manufacturer: ").strip()
    brand = input("- Insert brand: ").strip()
    cost = float(input("- Insert cost: ").strip())
    price = float(input("- Insert price: ").strip())
    print("Storing product details into the database...")
    cursor = DB_CONN.cursor()
    cursor.execute(PRODUCT_TABLE_CREATE)
    cursor.execute(PRODUCT_TABLE_INSERT, {"manufacturer": manufacturer, "brand": brand, "cost": cost, "price": price})
    DB_CONN.commit()
    DB_CONN.close()
    print("Program ending.")
    return None

if __name__ == "__main__":
  app = Main()