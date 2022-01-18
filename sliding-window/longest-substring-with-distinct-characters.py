def non_repeat_substring(str):
  l = 0
  maxlen = 0
  charset = set()
  for r in range(len(str)):
    if str[r] not in charset:
      charset.add(str[r])
    else:
      while str[l] != str[r]:
        charset.remove(str[l])
        l += 1
      l += 1
    maxlen = max(maxlen, r + 1 - l) 
  return maxlen