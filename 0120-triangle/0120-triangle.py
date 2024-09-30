class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        height = len(triangle)
        for i in range(height - 2, -1, -1):
            for j in range(len(triangle[i])):
                tobe_added = min(triangle[i + 1][j],triangle[i + 1][j + 1])
                triangle[i][j] += tobe_added
        return triangle[0][0]
        