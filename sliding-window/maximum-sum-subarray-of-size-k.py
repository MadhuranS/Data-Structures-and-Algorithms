def max_sub_array_of_size_k(k, arr):
  total = 0
  for i in range(k):
    total += arr[i]
  maxval = total
  for j in range(k, len(arr)):
    print(maxval)
    total = total - arr[j-k]+ arr[j]
    maxval = max(maxval, total)

  return maxval
