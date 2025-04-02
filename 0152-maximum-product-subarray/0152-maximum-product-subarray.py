class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curr_max = curr_min = 1
        for n in nums:
            temp_max = curr_max*n
            temp_min = curr_min*n
            curr_max = max(temp_max, temp_min, n)
            curr_min = min(temp_max, temp_min, n)
            ans = max(curr_max,ans)
        return ans

        