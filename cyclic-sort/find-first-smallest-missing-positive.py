def find_first_smallest_missing_positive(nums):
  i = 0

  while i < len(nums):
    j = nums[i] - 1
    if nums[i] > 0 and nums[i] <= len(nums) and nums[j] != nums[i]:
      nums[j], nums[i] = nums[i], nums[j]
    else:
      i += 1
  
  for i in range(len(nums)):
    if nums[i] != i + 1:
      return i + 1
  return -1
