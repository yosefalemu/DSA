class Solution:
    def grayCode(self, n: int) -> List[int]:
        def helper(path):
            if len(path) == n:
                return [path]
            a = helper(path + "0")
            b = helper(path + "1")
            b = b[::-1]
            return a + b
        res = helper("")
        return list(map(lambda x: int(x, 2), res))
        