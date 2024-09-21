class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_mapping = {}
        for c in nums:
            if c in majority_mapping:
                majority_mapping[c] += 1
            else:
                majority_mapping[c] = 1
        for key in majority_mapping:
            if majority_mapping[key] > len(nums) / 2:
                return key
                
        