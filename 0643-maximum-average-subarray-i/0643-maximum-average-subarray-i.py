class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 1
        n = len(nums)
        curr_sum = sum(nums[:k])
        ans = curr_sum / k
        while i + k <= n:
            curr_sum = curr_sum - nums[i - 1] + nums[i + k - 1]
            ans = max(ans, curr_sum/ k)
            i += 1
        return ans



        