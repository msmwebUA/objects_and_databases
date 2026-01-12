user_input = input("Insert number: ").strip()
try:
  number = float(user_input)
  print(f"Inserted value is '{number}'")
except ValueError:
  print("Oops! That wasn't valid number.")