import math

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A)
        max_point = -1000000007
        for i in range(n):
            dup = 1
            max_val= 0
            slope = {}
            for j in range(i+1,n):
                if A[i]==A[j] and B[i] == B[j]:
                    dup += 1
                else:
                    dx = A[j]-A[i]
                    dy = B[j]-B[i]
                    gcd = math.gcd(dx,dy)
                    dx = dx//gcd
                    dy = dy // gcd
                    key = str(dy)+'__'+str(dx)
                    if key in slope:
                        slope[key] += 1
                    else:
                        slope[key] = 1
                max_val = max(max_val,slope[key])
            max_point = max(max_val+dup,max_point)
        return max_point






if __name__ == '__main__':
    A = [3, 1, 4, 5, 7, -9, -8, 6]
    B = [4, -8, -3, -2, -1, 5, 7, -4]
    s = Solution()
    ans = s.solve(A,B)
    print(ans)