class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i = 1
        n = len(nums)
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        while i + k <= n:
            curr_sum = curr_sum - nums[i - 1] + nums[i + k -1]
            max_sum = max(max_sum, curr_sum)
            i += 1
        return max_sum / k



        