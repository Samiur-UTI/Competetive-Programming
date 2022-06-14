def minOp(word1,word2):
    word1Map = {}
    word2Map = {}
    commonList = []
    for i in range(len(word1)):
        word1Map[word1[i]] = i
    for i in range(len(word2)):
        word2Map[word2[i]] = i
        if word2[i] in word1Map:
            commonList.append(word2[i])
    if len(commonList) == 0:
        return len(word1) + len(word2)
    elif len(commonList) == 1:
        return len(word1) + len(word2) - 2
    else:
        print(commonList)
        

print(minOp("sea","ate"))