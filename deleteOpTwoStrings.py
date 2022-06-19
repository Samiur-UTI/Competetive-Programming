def minOp(word1, word2):
    m = len(word1)
    n = len(word2)
    counter = [[0]*(n+1) for x in range(m+1)]
    longest = 0
    lcs_set = set()
    for i in range(m):
        for j in range(n):
            if word1[i] == word2[j]:
                c = counter[i][j] + 1
                counter[i+1][j+1] = c
                if c > longest:
                    lcs_set = set()
                    longest = c
                    lcs_set.add(word1[i-c+1:i+1])
                elif c == longest:
                    lcs_set.add(word1[i-c+1:i+1])
    print(lcs_set)
    if len(lcs_set) == 0: return len(word1) + len(word2)
    return len(word1) + len(word2) - 2 * len(max(lcs_set))       

print(minOp("park","spake"))