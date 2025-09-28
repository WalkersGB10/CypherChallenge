alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

text = input("What is the plaintext?").upper()
key = input("What is the keyword?").upper()

cyphertext = ""

index = 0
for character in text:
  if character.isalpha():
    letter = alph.index(key[index % len(key)])
    letter += alph.index(character)
    letter = letter % 26
    cyphertext += alph[letter]
    index += 1
  else:
    cyphertext += character

print(cyphertext)
