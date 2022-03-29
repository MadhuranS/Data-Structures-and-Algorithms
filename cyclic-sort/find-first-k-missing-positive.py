def find_first_k_missing_positive(nums, k):
  missingNumbers = []
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i]>0 and nums[i] <= len(nums) and nums[i] != nums[j]:
      nums[j], nums[i] = nums[i], nums[j]
    else:
      i += 1
  
  extraNumbers = set()
  extraNumbers
  for i in range(len(nums)):
    if nums[i] != i + 1:
      missingNumbers.append(i + 1)
      extraNumbers.add(nums[i])
    if len(missingNumbers) == k:
      break
  
  x = len(nums)

  while len(missingNumbers) < k:
    print("Hello")
    x += 1
    if x not in extraNumbers:
      missingNumbers.append(x)
  return missingNumbers
