class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = []
        ans = []
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        def helper():
            if len(perm) == len(nums):
                ans.append(perm.copy())
                return
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    helper()
                    count[n] += 1
                    perm.pop()
        helper()
        return ans
        