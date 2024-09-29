class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        ans = 0
        for c in patterns:
            if c in word:
                ans += 1
        return ans
        