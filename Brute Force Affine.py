alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mults = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
inverses = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]

commonwords = ["HELLO ", "HELLO,", " THE ", " AND ", " THAT ", " HAVE ", " NOT ", " WITH ", " YOU ", " ARE ", " ALL ", " CIPHER ", "ING ", "ION ", " MEET ", " HARRY ", " JODIE ", " SHE ", " THIS ", " THAT ", " BUT ", " BECAUSE ", " WHAT ", " WHO ", " ABOUT ", " WHICH ", " WHEN ", " JACK ", " ALEX ", " IAN "]

cyphertext = input("What is the cyphertext?").upper()+" "
results = []
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
    results.append(result)
