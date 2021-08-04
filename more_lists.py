# append sum, making my list keep counting by adding two elements together
def append_sum(nums):
  nums.append(nums[-1] + nums[-2])
  nums.append(nums[-1] + nums[-2])
  nums.append(nums[-1] + nums[-2])
  return nums
append_sum([1, 2, 3, 4, 5])
print(append_sum([1, 2, 3, 4, 5]))

