class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        for item in s:
            if item in char_count:
                char_count[item] += 1
            else:
                char_count[item] = 1
        for item in t:
            if item in char_count:
                char_count[item] -= 1
            else:
                char_count[item] = 1
        for item in char_count.values():
            if item != 0:
                return False
        return True