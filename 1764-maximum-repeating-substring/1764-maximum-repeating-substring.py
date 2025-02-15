class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        while word * (ans + 1) in sequence:
            ans += 1
        return ans

