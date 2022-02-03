def find_word_concatenation(str, words):
  resultIndices = []
  if len(words) == 0 or len(str) == 0:
    return resultIndices
  
  wordLength = len(words[0])
  arrLength = len(words)
  wordFreq = {}
  for word in words:
    wordFreq[word] = wordFreq.get(word, 0) + 1

  for l in range(0, len(str) - (wordLength*arrLength) + 1):
    currFreq = {}
    for r in range(l + wordLength, l + wordLength*arrLength + 1, wordLength):
      word = str[r - wordLength:r]
      if word not in wordFreq:
        break
      currFreq[word] = currFreq.get(word, 0) + 1

      if currFreq[word] > wordFreq[word]:
        break
      if r == l + wordLength*arrLength:
        resultIndices.append(l)
  return resultIndices
