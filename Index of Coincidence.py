frequency = {}

text = input("What is the text?")
letters = 0

for character in text.upper():
  if character.isalpha():
    if character in frequency:
      frequency[character] += 1
    else:
      frequency[character] = 1
    letters += 1

probabilities = []
for key in frequency:
  if frequency[key] > 1:
    probability = (frequency[key] / letters) * ((frequency[key]-1) / (letters-1))
    print("Probablitiy of Coincidence of", key, "=", probability)
    probabilities.append(probability)
index = 0
for probability in probabilities:
  index += probability
print("Index of Coincidence is", index)
