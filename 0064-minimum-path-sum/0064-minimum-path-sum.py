class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        firstRow = grid[0]
        dp = []
        dp.append(firstRow[0])
        for i in range(1, len(firstRow)):
            dp.append(dp[i - 1] + firstRow[i])
        for j in range(1,len(grid)):
            currRow = grid[j]
            for k in range(len(currRow)):
                if k == 0:
                    dp[k] += grid[j][k]
                else:
                    dp[k] = grid[j][k] + min(dp[k - 1], dp[k])
        return dp[-1]
        