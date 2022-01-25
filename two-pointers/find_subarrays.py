from collections import deque

def find_subarrays(arr, target):
  
  # TODO: Write your code here
  if len(arr) == 0:
    return []

  result = []
  l = 0
  product = 1

  for r in range(len(arr)):
    right = arr[r]
    product *= right

    while product >= target and l < r:
      product /= arr[l]
      l += 1
    
    i = r
    temp = deque()
    while i >= l:
      temp.appendleft(arr[i])
      result.append(list(temp))
      i -= 1

  

  return result