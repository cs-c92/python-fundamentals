herbs_for_bunny = ["cilantro", "mint", "basil", "parsley", "sage", "rosemary"]
bunnys_favourite = "basil"
# break the list
for herb in herbs_for_bunny:
    print(herb)
    if herb == bunnys_favourite:
        print("That's his favourite!")
        break

num_list = [35, 62, 73, 42, 17, 19, 6, 41, 37, 24]
# continue printing
for num in num_list:
    if num > 31:
        continue
    print(num)

ice_cream_sales = [[25, 63, 64], [53, 77, 92], [85, 47, 20]]
ice_cream_sold = 0
# nested loops
for location in ice_cream_sales:
    print(location)
    for sold in location:
        ice_cream_sold += sold
print(ice_cream_sold)

numbers = [14, 10, 21, 45, 67]
print(numbers)
# intro to list comprehension
tripled = [nums * 3 for nums in numbers]
print(tripled)
halved = [halves / 2 for halves in tripled]
print(halved)
# rounding
halved_rounded = [round(ints) for ints in halved]
print(halved_rounded)
# conditionals
cond_eg = [num for num in numbers if num > 15]
print(cond_eg)
# squared and cubed
squared =[]
cubed = []
for num in numbers:
    print(num)
    squared.append(num**2)
    print(squared)
    cubed.append(num**3)
    print(cubed)

