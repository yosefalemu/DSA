class Solution:
    def maxArea(self, height: List[int]) -> int:
        leftpt = 0
        rightpt = len(height) - 1
        ans = 0
        while leftpt < rightpt:
            if height[leftpt] < height[rightpt]:
                ans = max(ans,(height[leftpt]*(rightpt-leftpt)))
                leftpt += 1
            elif height[leftpt] > height[rightpt]:
                ans = max(ans,(height[rightpt]*(rightpt-leftpt)))
                rightpt -= 1
            else:
                ans = max(ans,(height[leftpt]*(rightpt-leftpt)))
                leftpt += 1
        return ans
        
        
