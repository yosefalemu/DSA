class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for c in operations:
            if c.lstrip("-").isdigit():
                ans.append(int(c))
            elif c == "C":
                ans.pop()
            elif c == "D":
                ans.append(ans[-1]*2)
            else:
                ans.append(ans[-1] + ans[-2])
        return sum(ans)
        