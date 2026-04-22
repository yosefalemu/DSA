class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)

        for char, count in counts.items():
            if count == 1:
                return s.find(char)
        return -1
        