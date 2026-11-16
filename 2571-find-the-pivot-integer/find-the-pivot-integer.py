class Solution:
    def pivotInteger(self, n: int) -> int:
        x=int((n*(n+1)/2)**0.5)
        if x*x==n*(n+1)//2:
            return x
        return -1