class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        left=m-1
        right=n-1
        ans=m+n-1
        while right>=0:
            if left<0 or nums2[right]>nums1[left]:
                nums1[ans]=nums2[right]
                ans-=1
                right-=1
            else :
                nums1[ans]=nums1[left]
                left-=1
                ans-=1