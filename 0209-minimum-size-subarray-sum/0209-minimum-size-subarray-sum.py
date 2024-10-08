class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float("inf")
        leftpt = 0
        rightpt = 0
        pre_sum = 0
        while rightpt < len(nums):
            pre_sum += nums[rightpt]
            if pre_sum < target:
                rightpt += 1
            else:
                while pre_sum >= target:
                    ans = min(ans, rightpt - leftpt + 1)
                    pre_sum -= nums[leftpt]
                    leftpt += 1
                rightpt += 1
        return 0 if ans == float("inf") else ans
            
            
        
        
        