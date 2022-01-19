import math

def smallest_subarray_with_given_sum(s, arr):
  l = 0
  r = 0
  size = 1
  minsize = math.inf
  currsum = arr[l]

  while r < len(arr):
    if currsum < s:
      size += 1
      r += 1
      if r < len(arr):
        currsum += arr[r]
    else:
      minsize = min(minsize, size)
      l += 1
      size -= 1
      currsum -= arr[l - 1]

  if minsize == math.inf:
    return 0
  return minsize
