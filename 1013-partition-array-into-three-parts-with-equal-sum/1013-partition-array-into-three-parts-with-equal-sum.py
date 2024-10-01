class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total_sum = sum(arr)
        if total_sum % 3 != 0:
            return False
        each_sum = total_sum / 3
        ans = 0
        curr_sum = 0
        for c in arr:
            curr_sum += c
            if curr_sum == each_sum:
                ans += 1
                curr_sum = 0
            if ans == 3:
                return True
        return ans == 3