class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        listFormat = list(s)
        numItem = len(s)
        for i in range(0, numItem, 2*k):
            listFormat[i:k + i] = reversed(listFormat[i:k + i])
        return "".join(listFormat)
        