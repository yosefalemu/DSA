class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        ans = 0
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum == 0:
                ans += 1
        return ans
        