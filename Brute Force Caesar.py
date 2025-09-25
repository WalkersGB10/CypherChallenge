alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cyphertext = input("What is the cyphertext?").upper()

for i in range(1, 26):
  plaintext = ""
  for character in cyphertext:
    if character.isalpha():
      plaintext += alph[(alph.index(character)+i)%26].lower()
    else:
      plaintext += character
  print("Shift:", i)
  print("Plaintext:", plaintext)
  print()
