class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        ans = 0
        for c in freq_map:
            if c + 1 in freq_map:
                ans = max(ans,freq_map[c] + freq_map[c + 1])
        return ans
        