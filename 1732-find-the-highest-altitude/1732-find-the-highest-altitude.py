class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        ans_arr = [0]
        for c in gain:
            curr_height = ans_arr[-1]
            ans_arr.append(curr_height + c)
            ans = max(ans,ans_arr[-1])
        return ans
        