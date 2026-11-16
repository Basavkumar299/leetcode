class Solution:
    def pivotInteger(self, n: int) -> int:
        l=0
        r=n
        if n<=1:
            return n
        while l<=r:
            ans1=0
            ans2=0
            mid=(l+r)//2
            for i in range(1,mid+1):
                ans1=ans1+i
            for i in range(mid,n+1):
                ans2=ans2+i
            if ans1==ans2:
                return mid
            elif ans1>ans2:
                r=mid-1
            else : 
                l=mid+1
        return -1 
        
        