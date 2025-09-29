amount = int(input("How many subtexts?"))
subtexts = []
for i in range(amount):
  subtexts.append(input("What is subtext " + str(i+1)))

text=""
for i in range(len(subtexts[0])):
  for subtext in subtexts:
    if i < len(subtext):
      text += subtext[i]
print(text)
