class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        newColors = colors + colors[:2]
        numOfIterations = len(newColors) - 2
        ans = 0
        for i in range(numOfIterations):
            if newColors[i+1] != newColors[i] and newColors[i+1] != newColors[i+2]:
                ans += 1 
        return ans

        