class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        i = 0
        x = ""
        while i < len(str1) and i < len(str2):
            if str1[i] != str2[i]:
                return ""
            x += str1[i]
            if len(str1) % len(x) == 0 and len(str2) % len(x) == 0:
                mult1 = len(str1) // len(x)
                mult2 = len(str2) // len(x)
                if x*mult1 == str1 and x*mult2 == str2:
                    return x*math.gcd(mult1, mult2)
            i += 1
        return ""