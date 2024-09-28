class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1]*n
        if n < 2*k + 1:
            return ans
        window_sum = sum(nums[:2*k+1])
        for i in range(k,n - k):
            ans[i] = window_sum // (2*k + 1)
            if i + k + 1 < n:
                window_sum += nums[i + k + 1] - nums[i - k]
        return ans
            
        
            
            
            
            
        
        