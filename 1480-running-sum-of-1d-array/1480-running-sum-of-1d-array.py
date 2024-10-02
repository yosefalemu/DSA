class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        curr_sum = 0
        for i in range(len(nums)):
            curr_sum += nums[i]
            nums[i] = curr_sum
        return nums
        