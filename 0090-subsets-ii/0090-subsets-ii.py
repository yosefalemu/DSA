class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        sub = []
        count = {}
        nums.sort()
        def helper(i):
            if i == len(nums):
                key = tuple(sub)
                if key not in count:
                    ans.append(sub.copy())
                    count[key] = 1
                return 
            sub.append(nums[i])
            helper(i + 1)
            sub.pop()
            helper(i + 1)
        helper(0)
        return ans

        