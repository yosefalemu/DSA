class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 1
        lenWord1 = len(word1)
        lenWord2 = len(word2)
        i, j = 0, 0
        ans = ""
        while i < lenWord1 and j < lenWord2:
            if index % 2 == 1:
                ans += word1[i]
                i += 1
            else:
                ans += word2[j]
                j += 1
            index += 1
        if i < lenWord1:
            ans += word1[i:]
        if j < lenWord2:
            ans += word2[j:]
        return ans



        