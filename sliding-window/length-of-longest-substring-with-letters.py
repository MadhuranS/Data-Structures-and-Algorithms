def length_of_longest_substring(str, k):
  if len(str) <= k + 1:
    return len(str)
  
  l = 0
  chardict = {}
  maxlength = 0

  for r in range(len(str)):
    if str[r] not in chardict:
      chardict[str[r]] = 0
    chardict[str[r]] += 1

    if r - l + 1 - max(chardict.values()) > k:
      chardict[str[l]] -= 1
      l += 1
    else:
      maxlength = max(maxlength, r - l + 1)
  return maxlength
