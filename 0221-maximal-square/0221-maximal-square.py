class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_side = 0
        row = len(matrix)
        col = len(matrix[0])
        dp = [[0]*col for _ in range(row)]
        #Populate the initail column
        for i in range(col):
            dp[0][i] = int(matrix[0][i])
            if dp[0][i]:
                max_side = max(max_side,int(dp[0][i]))
        #Populate the initial row
        for i in range(row):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0]:
                max_side = max(max_side,int(dp[i][0]))
        for i in range(1,row):
            for j in range(1,col):
                if matrix[i][j] == "1":
                    dp[i][j] = min(dp[i - 1][j - 1],dp[i - 1][j], dp[i][j - 1]) + 1
                    max_side = max(max_side,dp[i][j])
        return max_side**2
        