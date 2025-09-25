alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
used = ""

cyphertext = input("What is the cyphertext?").upper()
keyword = input("What is the keyword?").upper()

key = ""

for character in keyword:
  if character not in used:
    key += character
    used += character

add = alph.index(key[-1])
for i in range(len(alph)):
  index = i
  index += add
  index = index % 26
  if alph[index] not in used:
    key += alph[index]

print(key)
plaintext = ""

unmap = {}
for i in range(26):
  unmap[key[i]] = alph[i]

print(unmap)

for character in cyphertext:
  if character.isalpha():
    plaintext += unmap[character]
  else:
    plaintext += character

print(plaintext)
