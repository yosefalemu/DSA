class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = float("inf")
        nums.sort()
        for c in nums:
            currNum = abs(c)
            if currNum < abs(ans) or (currNum == abs(ans) and c > 0):
                ans = c
        return ans

        