def totalFruit(self, fruits): 
    l = 0
    maxlen = 0
    fruitDict = {}
    fruitDict[fruits[l]] = 1
    counter = 1
    while counter < len(fruits) and fruits[counter] in fruitDict:
        counter+= 1
        fruitDict[fruits[l]] += 1

    if counter == len(fruits):
        return len(fruits)

    maxlen = counter + 1 - l
    fruitDict[fruits[counter]] = 1
    for r in range(counter + 1, len(fruits)):
        fruitDict[fruits[r]] = fruitDict.get(fruits[r], 0) + 1
        if fruitDict[fruits[r]] == 1:
            flag = True
            while flag:
                fruitDict[fruits[l]] -= 1
                if fruitDict[fruits[l]] == 0:
                    flag = False
                l += 1
        maxlen = max(r + 1 - l, maxlen)
    return maxlen
