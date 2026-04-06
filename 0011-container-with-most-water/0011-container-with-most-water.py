class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_pt = 0
        right_pt = len(height) - 1
        max_area = 0
        while left_pt < right_pt:
            curr_width = right_pt - left_pt
            curr_height = min(height[left_pt], height[right_pt])
            curr_area = curr_width*curr_height
            max_area = max(max_area, curr_area)
            if height[left_pt] > height[right_pt]:
                right_pt -= 1
            elif height[left_pt] < height[right_pt]:
                left_pt += 1
            else:
                left_pt += 1
                right_pt -= 1
        return max_area

