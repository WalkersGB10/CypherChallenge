text = input("What is the cyphertext?")
length = 5#int(input("How long is the key?"))

print(text)
print(length)

subtexts = []

for i in range(length):
  subtexts.append([])

index = 0
for character in text:
  if character.isalpha():
    subtexts[index % length].append(character)
    index += 1

for i in subtexts:
  print(i)
  print("\n\n\n")

