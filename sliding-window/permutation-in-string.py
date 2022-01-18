def find_permutation(str, pattern):
  if len(str) < len(pattern):
    return False
  l = 0
  counter = 0
  patternfreq = {}
  charfreq = {}
  
  while counter < len(pattern):
    patternfreq[pattern[counter]] = patternfreq.get(pattern[counter], 0) + 1
    charfreq[str[counter]] = charfreq.get(str[counter], 0) + 1
    counter += 1
  
  if charfreq == patternfreq:
    return True

  for r in range(counter, len(str)):
    charfreq[str[l]] -= 1
    if charfreq[str[l]] == 0:
      del charfreq[str[l]] 
    l += 1

    charfreq[str[r]] = charfreq.get(str[r], 0) + 1
    if charfreq == patternfreq:
      return True

  return False
    

