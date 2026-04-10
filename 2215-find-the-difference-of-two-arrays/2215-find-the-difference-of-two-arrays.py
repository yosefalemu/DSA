class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1_sets = set(nums1)
        num2_sets = set(nums2)
        ans = []
        temp1 = []
        for num1_set in num1_sets:
            if num1_set not in num2_sets:
                temp1.append(num1_set)
        temp2 = []
        for num2_set in num2_sets:
            if num2_set not in num1_sets:
                temp2.append(num2_set)
        return [temp1, temp2]


        