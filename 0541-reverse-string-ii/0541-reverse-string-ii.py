class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        reverseString = []
        lenStr = len(s)
        for i in range(0, lenStr, 2*k):
            reverseString.append(s[i:i + k][::-1])
            reverseString.append(s[i + k: i + 2*k])
        return "".join(reverseString)


        