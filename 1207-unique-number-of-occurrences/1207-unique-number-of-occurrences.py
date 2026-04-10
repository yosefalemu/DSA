class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_arr = dict()
        for num in arr:
            count_arr[num] = count_arr.get(num, 0) + 1
        return len(count_arr.values()) == len(set(count_arr.values()))



        