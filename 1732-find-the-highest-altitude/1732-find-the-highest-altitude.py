class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr_height = max_height = 0
        for gn in gain:
            curr_height += gn
            max_height = max(max_height, curr_height)
        return max_height
        