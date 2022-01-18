def longestOnes(self, arr, k):
        l = 0
        maxlen = 0
        numberOfOnes = 0
        for r in range(len(arr)):
            if arr[r] == 1:
                numberOfOnes += 1
            if r - l + 1 - numberOfOnes > k:
                while arr[l] == 1:
                    numberOfOnes -= 1
                    l += 1
                l+= 1
            else:
                maxlen = max(maxlen, r - l + 1)
        return maxlen