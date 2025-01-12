class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        char_count = {}
        for c in s:
            char_count[c] = char_count.get(c,0) + 1
        for i, c in enumerate(s):
            if char_count[c] < k:
                left = self.longestSubstring(s[:i],k)
                right = self.longestSubstring(s[i+1:],k)
                return max(left,right)
        return len(s)