class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count = {n:0 for n in nums}
        for n in nums:
            count[n] += 1
        ans = []
        def helper(path):
            if len(path) == len(nums):
                ans.append(path[:])
                return
            for num in count:
                if count[num] > 0:
                    path.append(num)
                    count[num] -= 1
                    helper(path)
                    count[num] += 1
                    path.pop()             
        helper([])
        return ans
        