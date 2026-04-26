class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = dict()
        for i in range(len(nums)):
            if target - nums[i] in temp:
                return [temp[target - nums[i]], i]
            temp[nums[i]] = i

