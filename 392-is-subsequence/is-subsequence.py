class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        n=len(s)
        m=len(t)
        while j<m and i<n:
            if s[i]==t[j]:
                i=i+1
            j=j+1
            
        return i==n
        