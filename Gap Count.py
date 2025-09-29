alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
gaps = {}

for i in alph:
  gaps[i] = [0]

text = input("What is your text?").upper()

for character in text:
  if character.isalpha():
    for i in gaps:
      gaps[i][-1] += 1
    gaps[character].append(0)

for i in gaps:
  print(i)
  print(gaps[i])
  print("\n\n")
