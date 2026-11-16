class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        n = len(arr)
        for i in range(n-2):
            if arr[i+1]-arr[i]!=arr[i+2]-arr[i+1]:
                return False        
        return True