def ioc(text):
  frequency = {}

  letters = 0

  for character in text.upper():
    if character.isalpha():
      if character in frequency:
        frequency[character] += 1
      else:
        frequency[character] = 1
      letters += 1

  probabilities = []
  test = 0
  for key in frequency:
    if frequency[key] > 0:
      probability = (frequency[key] / letters) * ((frequency[key]-1) / (letters-1))
      test += frequency[key] * (frequency[key]-1)
      #print("Probablitiy of Coincidence of", key, "=", probability)
      probabilities.append(probability)
  test = test / (letters * (letters-1))
  index = 0
  for probability in probabilities:
    index += probability
  #print("Index of Coincidence is", index)
  return test

cyphertext = input("What is the cyphertext?")

for k in range(1, 26):
  index = 0
  for i in range(0, k):
    text = ""
    ctext = ""
    for character in cyphertext:
      if character.isalpha():
        ctext += character
    
    for let in range(i, len(ctext), k):
      text += ctext[let]
    index += ioc(text)
  index /= k
  print("IOC at", k, "is", index)
