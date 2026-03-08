class Rot:

  def encrypt(self, plaintext: str, charkey: int, numkey: int) -> str:
    ciphertext = ""
    for char in plaintext:
      char_enc = self.shiftChar(char, charkey, numkey)
      ciphertext += char_enc
    return ciphertext

  def decrypt(self, ciphertext: str, charkey: int, numkey: int) -> str:
    plaintext = ""
    for char in ciphertext:
      # key must be negative for decryption
      char_dec = self.shiftChar(char, charkey * -1, numkey * -1)
      plaintext += char_dec
    return plaintext

  def shiftChar(self, char: str, charkey: int, numkey: int) -> str:
    # shift char using Unicode
    # char is letter in lowercase
    if "a" <= char <= "z":
      shifted_char = chr( ( (ord(char) - 97 + charkey) % 26 ) + 97 )
    # char is letter in uppercase
    elif "A" <= char <= "Z":
      shifted_char = chr( ( (ord(char) - 65 + charkey) % 26 ) + 65 )
    # char is digit
    elif "0" <= char <= "9":
      shifted_char = chr( ( (ord(char) - 48 + numkey) % 10 ) + 48 )
    # not alphabet or number char
    else:
      shifted_char = char
    return shifted_char