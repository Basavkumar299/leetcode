class Solution:
    def mySqrt(self, x: int) -> int:
        lt=0
        rt=x
        ans=x
        while lt<=rt:
            mid=(lt+rt)//2
            if mid*mid<=x:
                ans=mid
                lt=mid+1
            else:
                rt=mid-1
        return ans
                
        