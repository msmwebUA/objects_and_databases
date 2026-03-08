from sys import argv

def main() -> None:
  source = argv[1]
  dest = argv[2]
  print(f"Copying {source} to {dest}")
  with open(source, "rb") as f:
    data = f.read()
  with open(dest, "wb") as f:
    f.write(data)
  print("Copy operation completed!")

if __name__ == "__main__":
  main()