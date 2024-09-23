class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        leftpt, rightpt = 0, 0
        while rightpt < len(nums):
            if nums[leftpt] != 0:
                leftpt += 1
            elif nums[leftpt] == 0 and nums[rightpt] != 0:
                nums[leftpt], nums[rightpt] = nums[rightpt], nums[leftpt]
                leftpt += 1
            rightpt += 1