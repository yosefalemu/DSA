class Solution:
    def captureForts(self, forts: List[int]) -> int:
        ans = 0
        for fortPt, fortVal in enumerate(forts):
            if fortVal == 1:
                for i in range(fortPt - 1, -1, -1):
                    if forts[i] == 1:
                        break
                    elif forts[i] == -1:
                        ans = max(ans,fortPt - i - 1)
                        break
                for i in range(fortPt + 1,len(forts)):
                    if forts[i] == 1:
                        break
                    elif forts[i] == -1:
                        ans = max(ans, i - fortPt - 1)
                        break
        return ans
