class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        count = {}
        #count by increasing
        for num in target:
            count[num] = count.get(num, 0) + 1
        #count by decresing
        for num in arr:
            curr_num = count.get(num, 0)
            if curr_num == 0:
                return False
            else:
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
        return not count
        