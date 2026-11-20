class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        prefix=1
        ans=[1]*n
        suffix=1
        for i in range(n):
            ans[i]=prefix
            prefix=prefix*nums[i]
        for i in range(n-1,-1,-1):
            ans[i]=ans[i]*suffix
            suffix=suffix*nums[i]
        return ans
