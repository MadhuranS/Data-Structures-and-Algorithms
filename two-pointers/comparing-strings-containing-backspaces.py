def backspace_compare(str1, str2):
  idx1 = len(str1) - 1
  idx2 = len(str2) - 1

  while idx1 >= 0 or idx2 >= 0:
    idx1 = checkBackspace(str1, idx1)
    idx2 = checkBackspace(str2, idx2)
    print(idx1)

    if idx1 < 0 and idx2 < 0:
      return True
    elif idx1 < 0 or idx2 < 0:
      return False
    elif str1[idx1] != str2[idx2]:
      return False
    else:
      idx1 -= 1
      idx2 -= 1
  return True

def checkBackspace(word, idx):
  numOfBackspaces = 0
  
  while idx >= 0:
    if word[idx] == "#":
      numOfBackspaces += 1
    elif numOfBackspaces > 0:
      numOfBackspaces -= 1
    else:
      break
    idx -= 1
  return idx 

