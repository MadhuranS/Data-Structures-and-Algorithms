def triplet_with_smaller_sum(arr, target):
  count = 0
  arr.sort()
  print(arr)
  for i in range(len(arr) - 2):
    l = i + 1
    r = len(arr) - 1
    curr = arr[i]
    while l < r:
      left = arr[l]
      right = arr[r]
      print(curr, left, right)
      if curr + left + right < target:
        print("counted")
        count += 1 + (r - l - 1)
        l += 1
      else:
        r-= 1
  return count