def find_string_anagrams(str, pattern):
  l = 0
  patternFreq = {}
  strFreq = {}

  if len(pattern) > len(str):
    return []
  
  i = 0
  while i < len(pattern):
    patternFreq[pattern[i]] = patternFreq.get(pattern[i], 0) + 1
    strFreq[str[i]] = strFreq.get(str[i], 0) + 1
    i += 1

  result_indexes = []
  if patternFreq == strFreq:
    result_indexes.append(l)
  
  for r in range(i, len(str)):
    strFreq[str[l]] -= 1
    if strFreq[str[l]] == 0:
      del strFreq[str[l]] 
    l += 1

    strFreq[str[r]] = strFreq.get(str[r], 0) + 1

    if strFreq == patternFreq:
      result_indexes.append(l)

  return result_indexes

