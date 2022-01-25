def remove_duplicates(arr):
  # TODO: Write your code here
  temp = 1
  i = 1

  while i < len(arr):
    if arr[i] != arr[i-1]:
      arr[temp] = arr[i]
      temp += 1
    i += 1
  
  return temp