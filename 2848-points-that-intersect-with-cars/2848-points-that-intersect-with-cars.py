class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort(key=lambda x:x[0])
        ans = 0
        prev_end = -1
        for interval in nums:
            start, end = interval
            if start <= prev_end:
                if end > prev_end:
                    ans += end - prev_end        
            else:
                ans += end - start + 1
            prev_end = max(prev_end,end)
        return ans