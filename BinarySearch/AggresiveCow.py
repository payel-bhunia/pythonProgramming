def check(diff, A, B):
    first = 0
    count = 0
    for i in range(1, len(A)):
        if A[i] - A[first] >= diff:
            first = i
            count += 1
            if count == B-1:
                return True
    return False


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_diff = (max(A) - min(A)) // (B - 1)
        start = 1
        end = max_diff
        ans = -1
        while start <= end:
            mid = start + (end - start) // 2
            if check(mid, A, B):
                ans = mid
                start = mid + 1
            else:
                end = mid - 1
        return ans

if __name__ == "__main__":
    A = [1,2,3,4,5]
    B = 3
    s = Solution()
    print(s.solve(A,B))