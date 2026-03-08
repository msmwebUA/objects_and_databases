from sys import argv
from rot import Rot

class Main():
  def __init__(self) -> None:
    ciphertext = " ".join(argv[1:len(argv)])
    key = 13
    rot = Rot()
    plaintext = rot.decrypt(ciphertext, key)
    print(plaintext)
    return None

if __name__ == "__main__":
  app = Main()