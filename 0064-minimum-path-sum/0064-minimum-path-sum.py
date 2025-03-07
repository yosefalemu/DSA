class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        # Set the first column
        for i in range(1,rows):
            grid[i][0] += grid[i - 1][0]
        # Set the first row
        for j in range(1,cols):
            grid[0][j] += grid[0][j - 1]
        # Fill other slots accordingly
        for r in range(1, rows):
            for c in range(1, cols):
                grid[r][c] += min(grid[r][c - 1],grid[r - 1][c])
        return grid[rows - 1][cols -1]

        