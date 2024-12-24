class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans = -inf
        for i in range(len(nums)):
            count = 0
            temp = []
            for j in range(i,len(nums)):
                if count % 2 == 0 and nums[j] % 2 == 0 and nums[j] <= threshold:
                    temp.append(nums[j])
                    count += 1
                elif count % 2 != 0 and nums[j] % 2 != 0 and nums[j] <= threshold:
                    temp.append(nums[j])
                    count += 1
                else:
                    break
            ans = max(ans,len(temp))
        return ans
            
        