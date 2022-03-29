def cyclic_sort(nums):
  i = 0
  while i < len(nums):
    if nums[i] != i + 1:
      nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i]- 1]
    else:
      i += 1
  print(nums)
  return nums
