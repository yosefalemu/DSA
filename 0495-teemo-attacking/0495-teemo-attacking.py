class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        for i in range(len(timeSeries) - 1):
            gap =  timeSeries[i + 1] - timeSeries[i]
            if gap >= duration:
                ans += duration
            else:
                ans += gap
        return ans + duration
        