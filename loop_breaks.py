herbs_for_bunny = ["cilantro", "mint", "basil", "parsley", "sage", "rosemary"]
bunnys_favourite = "basil"

for herb in herbs_for_bunny:
    print(herb)
    if herb == bunnys_favourite:
        print("That's his favourite!")
        break

num_list = [35, 62, 73, 42, 17, 19, 6, 41, 37, 24]

for num in num_list:
    if num > 31:
        continue
    print(num)