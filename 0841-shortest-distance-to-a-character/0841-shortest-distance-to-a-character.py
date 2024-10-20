class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indexList = []
        for i in range(len(s)):
            if s[i] == c:
                indexList.append(i)
        ans = []
        j = 0
        for i in range(len(s)):
            if s[i] == c:
                ans.append(0)
                j += 1
            elif i < indexList[0]:
                ans.append(indexList[0] - i)
            elif i > indexList[-1]:
                ans.append(i - indexList[-1])
            else:
                ans.append(min(indexList[j] - i, i - indexList[j - 1]))
        return ans

        