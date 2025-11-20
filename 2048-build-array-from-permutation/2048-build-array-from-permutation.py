class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        temp = nums.copy()
        for i in range(len(nums)):
            nums[i] = temp[nums[i]]
        return nums
        