class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1,len(nums) + 1):
                increMovable = nums[:i] + nums[j:]
                if increMovable == sorted(increMovable) and len(increMovable) == len(set(increMovable)):
                    count += 1
        return count