class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(len(queries)):
            sum = 0
            count = 0
            for j in range(len(nums)):
                if sum + nums[j] > queries[i]:
                    break
                else:
                    sum += nums[j]
                    count += 1
            queries[i] = count
        return queries
                
        