import random
name = ""
question = "Will it rain?"
answer = ""
random_number = random.randint(1, 10)

if random_number == 1:
  answer = "Oh yeah, for sure."
elif random_number == 2:
    answer = "If I told you, I'd have to kill you."
elif random_number == 3:
    answer = "Signs point to groovy."
elif random_number == 4:
    answer = "I see many clouds."
elif random_number == 5:
    answer = "That is the big question!"
elif random_number == 6:
    answer = "No chance in hell."
elif random_number == 7:
    answer = "Don't count on it."
elif random_number == 8:
    answer = "Ow have mercy!"
elif random_number == 9:
    answer = "It doesn't matter."
elif random_number == 10:
    answer = "Ask again in klingon"
else:
  answer = "Error"

if name == "":
  print("Question: " + question)
else:
  print(name + " asks " + question)

if question == "":
  print("You gotta ask a question, man!")
else:

  print(" answer: " + answer)