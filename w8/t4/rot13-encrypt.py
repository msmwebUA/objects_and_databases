from sys import argv
from rot import Rot

class Main():
  def __init__(self) -> None:
    plaintext = argv[1]
    key = 13
    rot = Rot()
    ciphertext = rot.encrypt(plaintext, key)
    print(ciphertext)
    return None

if __name__ == "__main__":
  app = Main()