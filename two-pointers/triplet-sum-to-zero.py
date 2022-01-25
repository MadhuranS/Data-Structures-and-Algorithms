def search_triplets(arr):
  triplets = []
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

      if left + right + curr == 0:
        triplets.append([curr, left, right])
        l += 1
        r -= 1
        while arr[l] == arr[l-1] and l < r:
          l += 1
        while arr[r] == arr[r+1] and l < r:
          r -= 1

      elif left + right + curr >  0:
        r -= 1
      else:
        l += 1

  return triplets