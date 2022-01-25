import math
def triplet_sum_close_to_target(arr, target_sum):
  minval = math.inf
  difference = math.inf
  arr.sort()
  
  for i in range(len(arr) - 2):
    if i > 0 and arr[i] == arr[i - 1]:
      continue
    l = i + 1
    r = len(arr) - 1
    curr = arr[i]
    while l < r:
      left = arr[l]
      right = arr[r]
      if difference >= abs(curr + left + right - target_sum):
        if difference == abs(curr + left + right - target_sum):
          minval = min(minval, curr + left + right)
        else:
          minval = curr + left + right
        difference = abs(curr + left + right - target_sum)

      if curr + left + right == target_sum:
        return 0
      elif curr + left + right > target_sum:
        r -= 1
      else:
        l += 1

  return minval