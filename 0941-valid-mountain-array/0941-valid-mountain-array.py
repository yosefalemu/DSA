class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        max_index = arr.index(max(arr))
        if max_index == 0 or max_index == len(arr) - 1:
            return False
        for i in range(1, max_index + 1):
            if arr[i] <= arr[i - 1]:
                return False
        for i in range(max_index + 1, len(arr)):
            if arr[i] >= arr[i - 1]:
                return False
        return True




             

        