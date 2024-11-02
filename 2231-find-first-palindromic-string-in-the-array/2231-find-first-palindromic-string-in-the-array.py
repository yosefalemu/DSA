class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for c in words:
            if c == c[::-1]:
                return c
        return ""
        