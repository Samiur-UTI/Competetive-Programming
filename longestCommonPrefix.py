def longestCommonPrefix(strs):
    if not strs:
        return ""
    for i, letter in enumerate(strs[0]):
        for string in strs:
            if i >= len(string) or string[i] != letter:
                return string[:i]
    return strs[0]
print(longestCommonPrefix(['aaa','aa','aaa']))