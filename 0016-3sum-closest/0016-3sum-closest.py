class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans = float('inf')
        min_range = float('inf')
        for i in range(len(nums)):
            leftpt = i + 1
            rightpt = len(nums) - 1
            while leftpt < rightpt:
                current_sum = nums[i] + nums[leftpt] + nums[rightpt]
                diff = abs(target - current_sum)
                if diff < min_range:
                    min_range = diff
                    ans = current_sum
                if target - current_sum > 0:
                    leftpt += 1
                elif target - current_sum < 0:
                    rightpt -= 1
                else:
                    return current_sum
        return ans
        
        