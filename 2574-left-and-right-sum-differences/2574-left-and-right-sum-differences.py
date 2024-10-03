class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        right_sum = sum(nums)
        left_sum = 0
        for i in range(len(nums)):
            right_sum -= nums[i]
            temp = nums[i]
            nums[i] = abs(left_sum - right_sum)
            left_sum += temp
        return nums
        