class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = 0
        ansStr = ""
        for i in range(len(s)):
                left, right = i, i
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > ans:
                        ans = right - left + 1
                        ansStr = s[left: right + 1]
                    left -= 1
                    right += 1
                left, right = i, i + 1
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > ans:
                        ans = right - left + 1
                        ansStr = s[left: right + 1]
                    left -= 1
                    right += 1
        return ansStr

        