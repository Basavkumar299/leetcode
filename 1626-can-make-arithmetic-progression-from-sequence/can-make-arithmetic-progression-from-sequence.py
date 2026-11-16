class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        n = len(arr)
        i=0
        while i<n-2:
            if arr[i+1]-arr[i]!=arr[i+2]-arr[i+1]:
                return False
            i=i+1     
        return True