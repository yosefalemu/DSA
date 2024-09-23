class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique_numbers = set()
        nums_modify = []
        for c in nums:
            unique_numbers.add(c)
        for c in unique_numbers:
            nums_modify.append(c)
        nums_modify.sort()
        if len(nums_modify) >= 3:
            return nums_modify[-3]
        else:
            return nums_modify[-1]
        
        