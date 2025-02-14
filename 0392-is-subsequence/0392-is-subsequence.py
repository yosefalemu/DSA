class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        left = 0
        right = 0
        while left < len(s) and right < len(t):
            # if left == len(s) - 1:
            #     return True
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == len(s)
        