class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(tempNum):
            if len(tempNum) == 0:
                return [[]]
            perms = helper(tempNum[1:])
            res = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    p_copy = perm.copy()
                    p_copy.insert(i, tempNum[0])
                    res.append(p_copy)
            return res
        return helper(nums) 

            