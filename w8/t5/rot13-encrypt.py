from sys import argv
from rot import Rot

class Main():
  def __init__(self) -> None:
    plaintext = " ".join(argv[1:len(argv)])
    key = 13
    rot = Rot()
    ciphertext = rot.encrypt(plaintext, key)
    print(ciphertext)
    return None

if __name__ == "__main__":
  app = Main()