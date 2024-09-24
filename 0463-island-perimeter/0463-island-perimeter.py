class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        perimeter = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    perimeter += 4
                    if c > 0  and grid[r][c - 1] == 1:
                        perimeter -= 2
                    if r > 0 and grid[r - 1][c] == 1:
                        perimeter -= 2
        return perimeter
                
        