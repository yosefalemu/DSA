class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq_map = {}
        for c in nums:
            if c in freq_map:
                freq_map[c] += 1
            else:
                freq_map[c] = 1
        ans = 0
        for key, val in freq_map.items():
            if key + 1 in freq_map:
                ans = max(ans,val + freq_map[key + 1])
        return ans
        