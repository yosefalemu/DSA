class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if i > 0  and nums[i] == nums[i - 1]:
                continue
            leftpt = i + 1
            rightpt = len(nums) - 1
            while leftpt < rightpt:
                current = nums[i] + nums[leftpt] + nums[rightpt]
                if current == 0:
                    ans.append([nums[i],nums[leftpt],nums[rightpt]])
                    leftpt += 1
                    rightpt -= 1
                    while leftpt < rightpt and nums[leftpt] == nums[leftpt - 1]:
                        leftpt += 1
                    while leftpt < rightpt and nums[rightpt] == nums[rightpt + 1]:
                        rightpt -= 1
                elif current < 0:
                    leftpt += 1
                else:
                    rightpt -= 1
        return ans
                    
        