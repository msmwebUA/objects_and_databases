fname = input("Insert filename to read: ").strip()
try:
  with open(fname, encoding="utf-8") as f:
    print(f"#### {fname} content ####")
    print(f.read())
    print(f"#### {fname} content ####")
except FileNotFoundError:
  print(f"File '{fname}' not found.")
except Exception as err:
  print(f"Error occured: {err}")