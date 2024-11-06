class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        ans = 0
        for c in nums:
            if c - diff in nums and c + diff in nums:
                ans += 1
        return ans

        