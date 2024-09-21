class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        nums.sort()
        ans = 0
        for i in range(1,len(nums)):
            ans = max(ans,abs(nums[i] - nums[i - 1]))
        return ans
        