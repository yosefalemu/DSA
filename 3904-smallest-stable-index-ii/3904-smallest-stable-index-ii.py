class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_stab = [0]*len(nums)
        max_stab = [0]*len(nums)
        max_elm = -float('inf')
        min_elm = float('inf')
        for i in range(len(nums)):
            max_elm = max(max_elm, nums[i])
            max_stab[i] = max_elm
        for i in range(len(nums) - 1, -1, -1):
            min_elm = min(min_elm, nums[i])
            min_stab[i] = min_elm
        for i in range(len(nums)):
            if max_stab[i] - min_stab[i] <= k:
                return i
        return -1
        
            
            
        