def search_quadruplets(arr, target):
  quadruplets = []
  if len(arr) < 4:
    return quadruplets
  arr.sort()
  for i in range(len(arr) - 3):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    
    for j in range(i + 1, len(arr) - 2):
      if j > i + 1 and arr[j] == arr[j - 1]:
        continue
      
      first = arr[i]
      second = arr[j]
      l = j + 1
      r = len(arr) - 1

      while l < r:
        third = arr[l]
        fourth = arr[r]

        currsum = first  + second + third + fourth

        if currsum == target:
          quadruplets.append([first, second, third, fourth])
          l += 1
          while l < r and arr[l] == arr[l-1]:
            l += 1
          r -= 1
          while l < r and arr[r] == arr[r + 1]:
            r -= 1
        elif currsum < target:
          l += 1
        else:
          r -= 1
  return quadruplets
