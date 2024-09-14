class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ans = []
        if len(nums) < 4:
            return ans
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1,len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                leftpt = j + 1
                rightpt = len(nums) - 1
                while leftpt < rightpt:
                    current_sum = nums[i] + nums[j] + nums[leftpt] + nums[rightpt]
                    if current_sum == target:
                        ans.append([nums[i],nums[j],nums[leftpt],nums[rightpt]])
                        while leftpt < rightpt and nums[leftpt] == nums[leftpt + 1]:
                            leftpt += 1
                        while leftpt < rightpt and nums[rightpt] == nums[rightpt - 1]:
                            rightpt -= 1
                        leftpt += 1
                        rightpt -= 1
                    elif current_sum < target:
                        leftpt += 1
                    else:
                        rightpt -= 1
        return ans
        