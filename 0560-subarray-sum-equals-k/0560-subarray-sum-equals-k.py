class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count_dict = {0:1}
        count = 0
        pre_sum = 0
        for num in nums:
            pre_sum += num
            if pre_sum - k in count_dict:
                count += count_dict[pre_sum - k]
            if pre_sum in count_dict:
                count_dict[pre_sum] += 1
            else:
                count_dict[pre_sum] = 1
        return count
            