from db_conn import DB_CONN

class Product:
  manufacturer: str
  brand: str
  cost: float
  price: float

  def __init__(self, manufacturer: str, brand: str, cost: float, price: float):
    self.manufacturer = manufacturer
    self.brand = brand
    self.cost = cost
    self.price = price

  @staticmethod
  def createProduct() -> 'Product':
    print("Insert product details below:")
    manufacturer = input("- Insert manufacturer: ").strip()
    brand = input("- Insert brand: ").strip()
    cost = float(input("- Insert cost: ").strip())
    price = float(input("- Insert price: ").strip())
    return Product(manufacturer, brand, cost, price)

  def insertDB(self) -> None:
    create_table_stat = """
      CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        manufacturer VARCHAR(255) NOT NULL,
        brand VARCHAR(255) NOT NULL,
        cost REAL NOT NULL,
        price REAL NOT NULL
      )"""
    insert_product_stat = """
      INSERT INTO product (
          manufacturer, 
          brand, 
          cost, 
          price
        ) VALUES (
          :manufacturer, 
          :brand, 
          :cost, 
          :price
        );"""
    cursor = DB_CONN.cursor()
    cursor.execute(create_table_stat)
    cursor.execute(insert_product_stat, {
        'manufacturer': self.manufacturer,
        'brand': self.brand,
        'cost': self.cost,
        'price': self.price
      })
    DB_CONN.commit()

  @staticmethod
  def queryProducts(products: 'list[Product]' = []) -> 'list[Product]':
    select_products_stat = """
      SELECT * FROM product
      """
    cursor = DB_CONN.cursor()
    cursor.execute(select_products_stat)
    rows = cursor.fetchall()
    products = []
    for row in rows:
      products.append(Product(row["manufacturer"], row["brand"], row["cost"], row["price"]))
    return products