class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 = len(str1), len(str2)
        for i in range(min(len1, len2), 0, -1):
            if len1 % i == 0 and len2 % i == 0:
                candidate = str1[:i]
                if candidate*(len1 // i) == str1 and candidate*(len2 // i) == str2:
                    return candidate
        return ""



        