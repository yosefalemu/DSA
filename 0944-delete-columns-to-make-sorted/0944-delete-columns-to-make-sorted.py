class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        row = len(strs)
        col = len(strs[0])
        ans = 0
        for i in range(col):
            temp = strs[0][i]
            for j in range(1, row):
                if strs[j][i] < temp:
                    ans += 1
                    break
                temp = strs[j][i]
        return ans


        