class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        n = len(nums)
        max_left = [0]*n
        max_left[0] = nums[0]
        for i in range(1,n):
            max_left[i] = max(nums[i], max_left[i - 1])
        min_right = [0]*n
        min_right[n - 1] = nums[n - 1]
        for i in range(n - 2, -1, -1):
            min_right[i] = min(nums[i], min_right[i + 1])
        beauty = 0
        for i in range(1, n - 1):
            if nums[i] > max_left[i - 1] and nums[i] < min_right[i + 1]:
                beauty += 2
            elif nums[i] > nums[i - 1] and nums[i] < nums[i + 1]:
                beauty += 1
            else:
                pass
        return beauty

        