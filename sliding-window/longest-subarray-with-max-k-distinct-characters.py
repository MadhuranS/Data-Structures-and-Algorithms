def longest_substring_with_k_distinct(str1, k):
  if k >= len(str1):
    return len(str1)
  
  l = 0
  r = 0
  charset = {}
  numdistinct = 0
  maxsize = 0
  size = 0

  for i in range(len(str1)):
    if str1[r] in charset and charset[str1[r]] > 0:
      charset[str1[r]] += 1
    else:
      charset[str1[r]]= charset.get(str1[r],0) + 1
      numdistinct += 1

    if numdistinct > k:
      print("check")
      while charset[str1[l]] > 1:
        charset[str1[l]] -= 1
        l+= 1
      charset[str1[l]] -= 1
      l+= 1
      numdistinct -= 1
    print("what is maxsize", size)
    maxsize = max(r - l + 1, maxsize)
    r+= 1
  print("-----------", maxsize, str1, k)
  return maxsize
    
    
