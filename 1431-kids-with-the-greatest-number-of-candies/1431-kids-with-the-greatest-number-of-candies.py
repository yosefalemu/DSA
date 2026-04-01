class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        ans = []
        for candie in candies:
            if candie + extraCandies >= max_candie:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        