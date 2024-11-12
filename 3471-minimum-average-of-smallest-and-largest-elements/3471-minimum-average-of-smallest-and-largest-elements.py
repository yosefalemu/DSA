class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        leftPt = 0
        rightPt = len(nums) - 1
        ans = float("inf")
        while leftPt < rightPt:
            average = (nums[leftPt] + nums[rightPt])/2
            ans = min(ans,average)
            leftPt += 1
            rightPt -= 1
        return ans

        