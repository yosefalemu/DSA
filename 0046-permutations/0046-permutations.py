class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(tempNum):
            if len(tempNum) == 0:
                return [[]]
            res = []
            perms = helper(tempNum[1:])
            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i,tempNum[0])
                    res.append(perm_copy)
            return res
        return helper(nums)
 
            