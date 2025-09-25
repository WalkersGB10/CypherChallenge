frequency = {}

text = input("What is the text?")
letters = 0

for character in text.upper():
  if character.isalpha():
    if character in list(frequency.keys()):
      frequency[character] += 1
    else:
      frequency[character] = 1
    letters += 1

for key in frequency.keys():
  if frequency[key] > 1:
    probability = (frequency[key] / letters) * ((frequency[key]-1) / (letters-1)) * 2
    print("Probablitiy of Coincidence of", key, "=", probability)
