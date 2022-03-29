def find_corrupt_numbers(nums):
  # TODO: Write your code here
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1
    
  for i in range(len(nums)):
    if nums[i] != i + 1:
      return [nums[i], i + 1]
  return [nums[len(nums) - 1], len(nums)]