class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = 1
        prev = word[0]
        for i in range(1,len(word)):
            if prev == word[i]:
                ans += 1
            prev = word[i]
        return ans 




        