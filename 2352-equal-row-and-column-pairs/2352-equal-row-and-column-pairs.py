class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        row_dict = dict()
        for row in grid:
            row_dict[tuple(row)] = row_dict.get(tuple(row), 0) + 1
        for col in range(len(grid)):
            temp = []
            for row in range(len(grid)):
                temp.append(grid[row][col])
            if tuple(temp) in row_dict:
                ans += row_dict[tuple(temp)]
        return ans


        