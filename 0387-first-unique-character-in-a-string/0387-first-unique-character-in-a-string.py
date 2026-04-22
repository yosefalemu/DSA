class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)
        # We only iterate a maximum of 26 characters
        for char, count in counts.items():
            if count == 1:
                return s.find(char)
        return -1
        