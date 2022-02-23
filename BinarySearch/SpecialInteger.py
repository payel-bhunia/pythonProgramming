def check_Subarr(A, B, mid):
    summ = 0
    for i in range(mid):
        summ += A[i]
    j = mid
    i = 0
    while j < len(A):
        if summ > B:
            return False
        summ -= A[i]
        i += 1
        summ += A[j]
        j += 1
    if summ <= B:
        return True
    else:
        return False


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        low = 1
        high = len(A)
        res = 0
        while low <= high:
            mid = low + (high - low) // 2
            if check_Subarr(A, B, mid) == False:
                high = mid - 1
            else:
                res = mid
                low = mid + 1
        if check_Subarr(A, B, low) == False:
            return (low-1,res)
        else:
            return (low,res)

if __name__ == "__main__":
    A = [1,2,3,4,5]
    B = 10
    s = Solution()
    ans = s.solve(A,B)
    print(ans)