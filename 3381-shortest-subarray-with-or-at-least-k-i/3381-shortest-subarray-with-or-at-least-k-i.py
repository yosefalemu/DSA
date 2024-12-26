class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        ans = inf
        left = 0
        currOR = 0
        if k == 0:
            return 1
        for right in range(len(nums)):
            currOR |= nums[right]
            while currOR >= k:
                ans = min(ans,right - left + 1)
                currOR = 0
                for i in range(left + 1, right + 1):
                    currOR |= nums[i]
                left += 1
        return ans if ans != inf else -1

                
                 

        