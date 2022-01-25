def pair_with_targetsum(arr, target_sum):
  l = 0 
  r = len(arr) - 1

  while l < r:
    currsum = arr[l] + arr[r]
    if currsum < target_sum:
      l += 1
    elif currsum > target_sum:
      r -=1
    else:
      return [l, r]
    
  return []
