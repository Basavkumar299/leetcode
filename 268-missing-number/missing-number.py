class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        exp=(n*(n+1))/2
        act=sum(nums)
        return int(exp-act)