class Rot:

  def encrypt(self, plaintext: str, key: int) -> str:
    ciphertext = ""
    for char in plaintext:
      char_enc = self.shiftChar(char, key)
      ciphertext += char_enc
    return ciphertext

  def decrypt(self, ciphertext: str, key: int) -> str:
    plaintext = ""
    for char in ciphertext:
      # key must be negative for decryption
      char_dec = self.shiftChar(char, key * -1)
      plaintext += char_dec
    return plaintext

  def shiftChar(self, char: str, key: int) -> str:
    # shift char using Unicode
    # char is in lowercase
    if "a" <= char <= "z":
      shifted_char = chr( ( (ord(char) - 97 + key) % 26 ) + 97 )
    # char is in uppercase
    elif "A" <= char <= "Z":
      shifted_char = chr( ( (ord(char) - 65 + key) % 26 ) + 65 )
    # not alphabet char
    else:
      shifted_char = char
    return shifted_char
