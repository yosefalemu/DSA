class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums_modify = set()
        for c in nums:
            nums_modify.add(c)
        ans = []
        for i in range(1,len(nums) + 1):
            if i not in nums_modify:
                ans.append(i)
        return ans
        