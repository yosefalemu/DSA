class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        row_counts = Counter(tuple(row) for row in grid)
        for col in zip(*grid):
            ans += row_counts[col]
        return ans
        