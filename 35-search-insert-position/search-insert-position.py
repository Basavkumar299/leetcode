class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left=0
        n=len(nums)
        right=n-1
        ans=n
        while left<=right:
            mid=(left+right)//2
            if nums[mid]>=target:
                ans=mid
                right=mid-1
            else :
                left=mid+1
        return ans
