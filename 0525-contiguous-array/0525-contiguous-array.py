class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        count_dict = {0:-1}
        max_len = 0
        for i, num in enumerate(nums):
            count += 1 if num == 1 else -1
            if count in count_dict:
                max_len = max(max_len, i - count_dict[count])
            else:
                count_dict[count] = i
        return max_len
                
            