class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        count=1
        previous=0
        n=len(intervals)
        intervals.sort(key=lambda x:x[1])
        for i in range(1,n):
            if intervals[i][0]>=intervals[previous][1]:
                count+=1
                previous=i
        return n-count
        