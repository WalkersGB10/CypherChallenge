alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cyphertext = input("What is the cyphertext?").upper()
mult = int(input("What is the multiplier?"))
add = int(input("What is added?"))

plaintext = ""
def encrypt():
  result = ""
  for character in cyphertext:
    if character.isalpha():
      pos = alph.index(character)
      pos = (pos * mult + add) % 26
      result += alph[pos]
    else:
      result += character
  print(result)
  return result

def modular_inverse(multiplier, upper):
  for i in range(1, upper):
    if (multiplier * i) % upper == 1:
      return i
  return None

def decrypt(cyphertext):
  global mult
  inverse = modular_inverse(mult, 26)
  if inverse == None:
    return
  result = ""

  for character in cyphertext:
    if character.isalpha():
      pos = alph.index(character)
      pos = (inverse*(pos-add)) % 26
      result += alph[pos]
    else:
      result += character
  print(result)
  return result

plaintext = encrypt()
