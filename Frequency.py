alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
frequency = {}
letters = 0

for letter in alph:
  frequency[letter] = 0

for character in text.upper():
  if character.isalpha():
    if character in frequency:
      frequency[character] += 1
    else:
      frequency[character] = 1
    letters += 1
