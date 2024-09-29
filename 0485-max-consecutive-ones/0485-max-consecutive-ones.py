class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        count = 0
        for c in nums:
            if c == 1:
                count += 1
            else:
                ans = max(ans,count)
                count = 0
        if count:
            ans = max(ans,count)
        return ans
                
        