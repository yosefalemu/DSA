class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        nums.sort()
        leftpt = 0
        rightpt = len(nums) - 1
        mid = (leftpt + rightpt) // 2
        if mid != leftpt:
            return nums[mid]
        else:
            return -1
        