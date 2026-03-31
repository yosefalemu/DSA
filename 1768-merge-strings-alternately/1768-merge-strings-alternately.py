class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        leftpt = 0
        rightpt = 0
        result = ""
        while leftpt < len(word1) and rightpt < len(word2):
            result += word1[leftpt]
            result += word2[rightpt]
            leftpt += 1
            rightpt += 1
        if leftpt < len(word1):
            result += word1[leftpt:]
        if rightpt < len(word2):
            result += word2[rightpt:]
        return result

        # let n = len(word1)
        # let m = len(word2)
        # let p = max(n, m)
        # time complexity O(p) which equivalent with O(p)
        # space complexity O(n + m) which is equivalent with O(n)



        