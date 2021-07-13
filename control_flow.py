print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 1
relative_weight = 0

print(relative_weight)
# Write an if statement below:
if planet == 3:
  relative_weight = 2.34 * weight
elif planet == 1:
  relative_weight = 0.91 * weight
elif planet == 2:
  relative_weight = 0.38 * weight
elif planet == 4:
  relative_weight = 1.06 * weight
elif planet == 5:
  relative_weight = 0.92 * weight
elif planet == 6:
  relative_weight = 1.19 * weight
print(relative_weight)
