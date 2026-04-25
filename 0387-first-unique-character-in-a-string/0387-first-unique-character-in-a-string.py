class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = Counter(s)

        for key in counts.keys():
            if counts[key] == 1:
                return s.find(key)
        return -1
        