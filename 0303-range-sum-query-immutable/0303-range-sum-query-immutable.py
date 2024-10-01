class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        curr_sum = 0
        for c in nums:
            curr_sum += c
            self.prefix_sum.append(curr_sum)
        

    def sumRange(self, left: int, right: int) -> int:
        if left != 0:
            prefix_left_sum = self.prefix_sum[left - 1]
        else:
            prefix_left_sum = 0
        prefix_right_sum = self.prefix_sum[right]
        return prefix_right_sum - prefix_left_sum
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)