class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq_map = {}
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        ans = 0
        for key,val in freq_map.items():
            if key + 1 in freq_map:
                ans = max(ans,val + freq_map[key + 1])
        return ans
        