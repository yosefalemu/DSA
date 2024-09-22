class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        rangeArr = [0]
        ans = []
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1] + 1:
                rangeArr.append(i)
            else:
                if len(rangeArr) == 1:
                    ans.append(str(nums[rangeArr[0]]))
                else:
                    ans.append(str(nums[rangeArr[0]]) + "->" + str(nums[rangeArr[-1]]))
                rangeArr = [i]
        if len(rangeArr) == 1:
            ans.append(str(nums[rangeArr[0]]))
        else:
            ans.append(str(nums[rangeArr[0]]) + "->" + str(nums[rangeArr[-1]]))
        return ans
        
                    
                    
            
        