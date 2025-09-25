alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cyphertext = input("What is the cyphertext?").upper()
shift = int(input("What is the shift?"))

plaintext = ""
for character in cyphertext:
  if character.isalpha():
    plaintext += alph[(alph.index(character) + shift) % 26].lower()
  else:
    plaintext += character
print(plaintext)
