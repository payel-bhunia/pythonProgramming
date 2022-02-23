def get_LCM(B,C):
    if B > C:
        high = B
        low = C
    else:
        high = C
        low = B
    while low:
        high, low = low, high%low
    gcd = high
    return (B*C//gcd)
class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        mod = 1000000007
        low = 1
        high = A * min(B,C)
        lcm = get_LCM(B,C)
        while low <= high:
            mid = low+(high-low)//2
            if (mid//B)+(mid//C)-(mid//lcm) > A:
                high = mid-1
            elif (mid//B)+(mid//C)-(mid//lcm) < A:
                low = mid+1
            else:
                high = mid-1
        if low > high:
            return high+1


if __name__ == "__main__":
    A = 19
    B = 11
    C = 13
    s = Solution()
    ans = s.solve(A,B,C)
    print(ans)