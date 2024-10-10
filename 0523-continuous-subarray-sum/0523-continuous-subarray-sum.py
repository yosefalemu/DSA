class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        index_dic = {0:-1}
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            if remainder in index_dic:
                if i - index_dic[remainder] > 1:
                    return True
            else:
                index_dic[remainder] = i
        return False