class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # Hash map to store the first occurrence of each remainder
        remainder_map = {0: -1}
        prefix_sum = 0
        
        for i, num in enumerate(nums):
            prefix_sum += num
            remainder = prefix_sum % k
            
            if remainder in remainder_map:
                if i - remainder_map[remainder] > 1:
                    return True
            else:
                remainder_map[remainder] = i
        
        return False