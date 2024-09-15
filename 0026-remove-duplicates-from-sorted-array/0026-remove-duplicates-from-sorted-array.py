class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slowpt = 0
        for fastpt in range(len(nums)):
            if nums[slowpt] != nums[fastpt]:
                nums[slowpt + 1] = nums[fastpt]
                slowpt += 1
            else:
                fastpt += 1
        return slowpt + 1