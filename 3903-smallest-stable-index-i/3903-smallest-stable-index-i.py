class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        for i in range(len(nums)):
            max_stab = max(nums[:i + 1])
            min_stab = min(nums[i:])
            if max_stab - min_stab <= k:
                return i
        return -1
        