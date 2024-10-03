class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        ans = 0
        curr_subarr_len = 1
        odd_num_seq = 0
        while curr_subarr_len <= len(arr):
            curr_sum = 0
            range_togo = len(arr) + 1 - curr_subarr_len
            for i in range(range_togo):
                curr_sum += sum(arr[i: i + curr_subarr_len])
            ans += curr_sum
            odd_num_seq += 1
            curr_subarr_len = ((2 * odd_num_seq) + 1)
        return ans
        