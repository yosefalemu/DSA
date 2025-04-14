class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        comb = []
        temp = [i for i in range(1, n + 1)]

        def helper(start):
            if len(comb) == k:
                ans.append(comb.copy())
                return
            for i in range(start, n):
                comb.append(temp[i])
                helper(i + 1)
                comb.pop()

        helper(0)
        return ans