# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        n = len(intervals)
        intervals.sort(key = lambda x:x.start)
        i = 1
        ans = []
        curr = intervals[0]
        flag = 0
        while i < n:
            if intervals[i].start > curr.end:
                ans.append(curr)
                curr = intervals[i]
                flag = 0
            elif intervals[i].start == curr.start:
                curr.end = max(intervals[i].end,curr.end)
                flag = 1
            elif intervals[i].start <= curr.end:
                curr.end = max(intervals[i].end,curr.end)
                flag = 1
            i+=1
        ans.append(curr)
        return ans

s = Solution()
A = [(1,2),(1,4),(4,5),(8,9),(6,7)]
inp = []
for i in A:
    node = Interval(i[0],i[1])
    inp.append(node)
ans = s.merge(inp)
for i in ans:
    print(i.start,i.end)

