class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slowpt = 0
        for fastpt in range(len(nums)):
            if nums[fastpt] != val:
                nums[slowpt] = nums[fastpt]
                slowpt += 1
        return slowpt
        