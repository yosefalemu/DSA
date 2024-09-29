class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        newHeight = sorted(heights)
        ans = 0
        for i in range(len(heights)):
            if heights[i] != newHeight[i]:
                ans += 1
        return ans
        