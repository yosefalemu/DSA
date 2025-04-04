class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        def helper(subExp):
            if subExp.isdigit():
                return [int(subExp)]
            result = []
            for idx, char in enumerate(subExp):
                if char in "+-*":
                    leftSubExp = helper(subExp[:idx])
                    rightSubExp = helper(subExp[idx + 1:])
                    for leftNum in leftSubExp:
                        for rightNum in rightSubExp:
                            if char == "+":
                                result.append(leftNum + rightNum)
                            elif char == "-":
                                result.append(leftNum - rightNum)
                            elif char == "*":
                                result.append(leftNum * rightNum)
            return result
        return helper(expression)

        