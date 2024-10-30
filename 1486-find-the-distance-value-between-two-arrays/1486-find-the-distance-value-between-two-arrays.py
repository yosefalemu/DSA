class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans = 0
        for num1 in arr1:
            notFound = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    notFound = False
                    break
            if notFound:
                ans += 1
        return ans
                




        