class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        leftpt = 0
        pre_sum = 0
        for rightpt in range(len(nums)):
            pre_sum += nums[rightpt]
            while pre_sum >= target:
                ans = min(ans, rightpt - leftpt + 1)
                pre_sum -= nums[leftpt]
                leftpt += 1
        return 0 if ans == float("inf") else ans

            
            
        
        
        