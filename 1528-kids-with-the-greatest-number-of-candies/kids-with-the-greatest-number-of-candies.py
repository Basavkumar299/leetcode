class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        return [candie+extraCandies>=maximum for candie in candies]
