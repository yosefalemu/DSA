class Solution:
    def distinctDifferenceArray(self, nums: List[int]) -> List[int]:
        ans = []
        left_counter = {}
        right_counter = {}
        for num in nums:
            if num in right_counter:
                right_counter[num] += 1
            else:
                right_counter[num] = 1
        for num in nums:
            if num in left_counter:
                left_counter[num] += 1
            else:
                left_counter[num] = 1
            right_counter[num] -= 1
            if right_counter[num] == 0:
                del right_counter[num]
            ans.append(len(left_counter) - len(right_counter))
        return ans

        