class Solution:
    def lowerbound(self, nums:list[int],target:int)->int:
        left=0
        n=len(nums)
        right=n-1
        ans1=n
        while left<=right:
            mid =(left+right)//2
            if nums[mid]>=target:
                ans1=mid
                right=mid-1
            else: left=mid+1
        return ans1
    def upperbound(self, nums:list[int],target:int)->int:
        left=0
        n=len(nums)
        right=n-1
        ans2=n
        while left<=right:
            mid =(left+right)//2
            if nums[mid]>target:
                ans2=mid
                right=mid-1
            else: left=mid+1
        return ans2
    
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lb=self.lowerbound(nums,target)
        ub=self.upperbound(nums,target)
        if lb!=ub:
            return [lb,ub-1]
        else:
            return [-1,-1]
        