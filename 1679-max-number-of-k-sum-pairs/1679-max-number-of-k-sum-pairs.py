class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left_pt = 0
        right_pt = len(nums) - 1
        ans = 0
        
        while left_pt < right_pt:
            current_sum = nums[left_pt] + nums[right_pt]
            
            if current_sum == k:
                ans += 1
                left_pt += 1
                right_pt -= 1
            elif current_sum > k:
                right_pt -= 1
            else:
                left_pt += 1
                
        return ans