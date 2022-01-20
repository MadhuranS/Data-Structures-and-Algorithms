import math

def find_substring(str, pattern):
  if len(pattern) > len(str):
    return ""

  origFreq = {}

  for char in pattern:
    origFreq[char] = origFreq.get(char, 0) + 1

  currFreq = {}
  required = len(origFreq)
  l = 0
  satisfied = 0
  startIndex = 0
  minlen = len(str) + 1

  for r in range(len(str)):
    char = str[r]
    if char in origFreq:
      currFreq[char] = currFreq.get(char, 0) + 1
      if currFreq[char] == origFreq[char]:
        satisfied += 1
    
    while satisfied == required:
      if r - l + 1 < minlen:
        minlen = r-l+1
        startIndex = l
      if str[l] in currFreq:
        currFreq[str[l]] -= 1
        if currFreq[str[l]] < origFreq[str[l]]:
          satisfied -= 1
      l += 1
  
  if minlen > len(str):
    return ""
  return str[startIndex: startIndex + minlen]
      

  
