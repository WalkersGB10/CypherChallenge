from math import sqrt
def calc_frequency(text, results):
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

  probabilities = {}
  expected = {"E": 0.127, "T": 0.0906, "A": 0.0817, "O": 0.0751, "I": 0.0697, "N": 0.0675, "R": 0.0599, "S": 0.0633, "H": 0.0609, "L": 0.0403}

  for key in frequency:
    if key in "ETAOINRSHL":
      probabilities[key] = frequency[key] / letters
  
  score = 0
  for key in expected:
    standard_deviation = sqrt((expected[key] * (1-expected[key])) / letters)
    z_score = abs((probabilities[key] - expected[key]) / standard_deviation)
    score += z_score
  score = score / 10
  if score < 1:
    results[text] = score
  return results




alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mults = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
inverses = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

commonwords = ["HELLO ", "HELLO,", " THE ", " AND ", " THAT ", " HAVE ", " NOT ", " WITH ", " YOU ", " ARE ", " ALL ", " CIPHER ", "ING ", "ION ", " MEET ", " HARRY ", " JODIE ", " SHE ", " THIS ", " THAT ", " BUT ", " BECAUSE ", " WHAT ", " WHO ", " ABOUT ", " WHICH ", " WHEN "]

cyphertext = input("What is the cyphertext?").upper()+" "
results = {}
for index in range(12):
  for add in range(25):
    common = False
    result = ""
    for character in cyphertext:
      if character.isalpha():
        pos = alph.index(character)
        pos -= (add+1)
        pos *= inverses[index]
        result += alph[pos%26]
      else:
        result += character
    for word in commonwords:
      if word in result:
        common = True
    if common == True:
      print(inverses[index], add)
      print(result)
    results = calc_frequency(result, results)

print("There are", len(list(results.keys())), "low z scores")
ans = input("Need to see low z scores?")
if ans[0].lower() == "y":
  print(len(list(results.keys())))
  for result in results:
    print(result, results[result])
