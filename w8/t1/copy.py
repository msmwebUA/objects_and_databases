def main() -> None:
  print("Welcome to the copy utility.")
  source = input("Insert source filepath: ").strip()
  dest = input("Insert destination filepath: ").strip()
  with open(source, "rb") as f:
    data = f.read()
  with open(dest, "wb") as f:
    f.write(data)
  print("Copy operation completed!")

if __name__ == "__main__":
  main()