# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param newInterval, a Interval
    # @return a list of Interval
    def insert(self, intervals, newInterval):
        n = len(intervals)
        l = newInterval[0]
        r = newInterval[1]
        mergeInt = []
        ans = []
        for i in range(n):
            if l <= intervals[i][1] and intervals[i][0] <= l:
                if r <= intervals[i][1]:
                    return intervals
                else:
                    mergeInt.append(i)
            else:
                ans.append(intervals[i])
            if r >= intervals[i][0] and r <= intervals[i][1]:
                mergeInt.append(i)
            if i != n - 1:
                if l >= intervals[i][1] and r <= intervals[i + 1][0]:
                    ans.append(i + 1, [l, r])
            else:
                if l >= intervals[i][1]:
                        ans.append([l, r])
        if len(mergeInt) > 0:
            ans.insert(mergeInt[0],[min(l,mergeInt[0][0]),max(r,mergeInt[-1][1])])
        return ans


if __name__ == '__main__':
    A = [[1, 3], [6, 9]]
    B = [2,5]
    s= Solution()
    n = s.insert(A, B)
    print(n)





