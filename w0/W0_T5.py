summa = 0.0
print(f"Current value {summa}")
while True:
  user_input = input("Add number(empty stops): ").strip()
  if not user_input:
    print(f"Final value {summa}")
    break
  else:
    summa += float(user_input)
    print(f"Current value {summa}")
