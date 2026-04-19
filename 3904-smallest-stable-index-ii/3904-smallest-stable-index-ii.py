class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        min_stab = [0]*n
        min_ele = nums[-1]

        for i in range(n - 1, -1, -1):
            min_ele = min(min_ele, nums[i])
            min_stab[i] = min_ele
        
        max_ele = -float('inf')
        for i in range(n):
            max_ele = max(max_ele, nums[i])
            nums[i] = max_ele
            if max_ele - min_stab[i] <= k:
                return i
        
        return -1

        

        
            
            
        