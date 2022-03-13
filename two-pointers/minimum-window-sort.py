import math

def shortest_window_sort(arr):
  l = 1
  r = len(arr) - 2
  while l <= r and (arr[l] > arr[l - 1] or arr[r] < arr[r + 1]):
    if not arr[l] < arr[l - 1]:
      l += 1
    
    if not arr[r] > arr[r + 1]:
      r -= 1
    
  if r < l:
    return 0

  minval = math.inf
  maxval = -math.inf
  for i in range(l,r + 1):
    minval = min(minval, arr[i])
    maxval = max(maxval, arr[i])
  
  left = l
  for i in range(l, -1, -1):
    if minval < arr[i]:
      left = i
  
  right = r
  for i in range(r, len(arr)):
    if maxval > arr[i]:
      right = i
      
  return right - left + 1