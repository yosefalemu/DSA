class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        for i in range(len(nums)):
            intial = 0
            for j in range(i,len(nums)):
                intial |= nums[j] 
                if intial >= k:
                    ans = min(ans,j - i + 1)
                    break
        return ans if ans != inf else -1
                
                 

        