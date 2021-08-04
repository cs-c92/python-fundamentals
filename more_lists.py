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
