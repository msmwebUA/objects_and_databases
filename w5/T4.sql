CREATE TABLE product (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL UNIQUE,
  price_per_kilo NUMERIC NOT NULL
);

CREATE TABLE receipt (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  cashier TEXT NOT NULL,
  created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_receipt (
  amount NUMERIC NOT NULL,
  product_id INTEGER NOT NULL REFERENCES product (id),
  receipt_id INTEGER NOT NULL REFERENCES receipt (id)
);

.mode csv
.import --skip 1 t4_product.csv product
.import --skip 1 t4_receipt.csv receipt
.import --skip 1 t4_product_receipt.csv product_receipt