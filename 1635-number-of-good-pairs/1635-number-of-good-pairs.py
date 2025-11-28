class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counts = Counter(nums)
        ans = 0
        for value in counts.values():
            ans += value * (value - 1) // 2
        return ans


        