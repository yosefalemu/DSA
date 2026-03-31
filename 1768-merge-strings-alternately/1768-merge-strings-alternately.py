class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        result = ""
        while i < len(word1) and i < len(word2):
            result += word1[i]
            result += word2[i]
            i += 1
        if i < len(word1):
            result += word1[i:]
        if i < len(word2):
            result += word2[i:]
        return result

        # let n = len(word1)
        # let m = len(word2)
        # time complexity O(n + m)
        # space complexity O(n + m)



        