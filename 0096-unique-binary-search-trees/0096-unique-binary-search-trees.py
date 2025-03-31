class Solution:
    def numTrees(self, n: int) -> int:
        if n == 1:
            return 1
        ans = [0]*(n + 1)
        #bases cases
        ans[0] = 1
        ans[1] = 1
        for i in range(2,len(ans)):
            for j in range(i):
                ans[i] += ans[j]*ans[i - 1 - j]
        return ans[-1]
        