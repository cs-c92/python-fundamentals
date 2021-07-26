for number in range(3):
    print("Test", number + 1)

summon = "Beetlejuice!"
for s in range(3):
    print(summon)


countdown = 5
while countdown >= 1:
    print(countdown, (countdown - 1) * "."); countdown -= 1
print("Thunderbirds are go!")


feed_the_bunny = ["Hay", "Kale", "Nuggets", "Herbs"]
length = len(feed_the_bunny)
index = 0
while index < length:
  print("You can feed a bunny " + feed_the_bunny[index])
  index += 1
