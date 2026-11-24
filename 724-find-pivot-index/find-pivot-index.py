class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        total_sum=sum(nums)
        l_sum=0
        for i  in range(n):
            if l_sum==total_sum-nums[i]-l_sum:
                return i
            l_sum=l_sum+nums[i]
        return -1
