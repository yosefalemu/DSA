class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candie = max(candies)
        return [candy + extraCandies >= max_candie for candy in candies]

        