class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        intial = 0
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                intial = intial | nums[j]
                if intial >= k:
                    ans = min(ans,j - i + 1)
                    break
            intial = 0
        return ans if ans != inf else -1
                
                 

        