class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        if len(s) < 3:
            return ans
        numOfIteration = len(s) - 2
        for i in range(numOfIteration):
            temp = s[i:i+3]
            if len(set(temp)) == len(temp):
                ans += 1
        return ans
        
        