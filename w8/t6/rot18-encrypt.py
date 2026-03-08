from sys import argv
from rot import Rot

class Main():
  def __init__(self) -> None:
    plaintext = " ".join(argv[1:len(argv)])
    charkey = 13
    numkey = 5
    rot = Rot()
    ciphertext = rot.encrypt(plaintext, charkey, numkey)
    print(ciphertext)
    return None

if __name__ == "__main__":
  app = Main()