# append sum, making my list keep counting by adding two elements together

def append_sum(nums):
  nums.append(nums[-1] + nums[-2])
  nums.append(nums[-1] + nums[-2])
  nums.append(nums[-1] + nums[-2])
  return nums
append_sum([1, 2, 3, 4, 5])
print(append_sum([1, 2, 3, 4, 5]))

# ifs and lists
def two_lists(one, two):
    if len(one) >= len(two):
        return one[-1]
    else:
        return two[-1]
two_lists([2, 4, 6, 8, 10], [1, 3, 4, 7, 9])
print(two_lists([2, 4, 6, 8, 10], [1, 3, 4, 7, 9]))

# count and if
def favourite_flavours(list, item, n):
    if list.count(item) > n:
        return True
    else:
        return False
favourite_flavours(["strawberry", "chocolate", "mint", "mint", "pistachio", "chocolate", "mint"], "mint", 2)
print(favourite_flavours(["strawberry", "chocolate", "mint", "mint", "pistachio", "chocolate", "mint"], "mint", 2))

# sort two lists
def sorting_lists(one, two):
    mixed = one + two
    fixed = sorted(mixed)
    print(fixed)
sorting_lists([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
