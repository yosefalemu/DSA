class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        col = len(grid[0])
        row = len(grid)
        ans = 0
        while col > 0:
            all_max = 0
            row_max = 0
            for row in grid:
                curr_max = max(row)
                row.remove(curr_max)
                row_max = max(row_max, curr_max)
            ans += row_max
            col -= 1
        return ans
            
        