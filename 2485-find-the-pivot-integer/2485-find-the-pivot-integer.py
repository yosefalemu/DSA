class Solution:
    def pivotInteger(self, n: int) -> int:
        left_sum = 0
        right_sum = (n*(n + 1))/2
        for num in range(1, n + 1):
            left_sum += num
            if left_sum == right_sum:
                return num
            right_sum -= num
        return -1
            
        