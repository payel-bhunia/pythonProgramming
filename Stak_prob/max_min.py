def find_nearest_greater(A, n, left_g, right_g):
    cl = []
    for i in range(n):
        while len(cl) > 0 and A[cl[-1]] < A[i]:
            cl.pop()
        if len(cl) == 0:
            left_g.append(-1)
        else:
            left_g.append(cl[-1])
        cl.append(i)
    cl = []
    i = n-1
    while i > -1:
        while len(cl) > 0 and A[cl[-1]] <= A[i]:
            cl.pop()
        if len(cl) != 0:
            right_g[i] = cl[-1]
        cl.append(i)
        i -= 1

def find_nearest_smaller(A,n,left_s, right_s):
    cl = []
    for i in range(n):
        while len(cl) > 0 and A[cl[-1]] > A[i]:
            cl.pop()
        if len(cl) == 0:
            left_s.append(-1)
        else:
            left_s.append(cl[-1])
        cl.append(i)
    cl=[]
    i = n-1
    while i > -1:
        while len(cl) > 0 and A[cl[-1]] >= A[i]:
            cl.pop()
        if len(cl) != 0:
            right_s[i] = cl[-1]
        cl.append(i)
        i -= 1



class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        left_s = []
        right_s = [-1] * n
        left_g = []
        right_g = [-1] * n
        find_nearest_smaller(A,n, left_s, right_s)
        find_nearest_greater(A, n, left_g, right_g)
        print(A)
        print(left_s)
        print(right_s)
        print(left_g)
        print(right_g)
        max_c = 0
        min_c = 0
        for i in range(n):
            if left_g[i] == -1:
                size1 = i-0+1
            else:
                size1 = i - left_g[i]
            if right_g[i] == -1:
                size2 = n - i
            else:
                size2 = right_g[i] - i
            max_c += A[i] * size2 *size1
        for i in range(n):
            if left_s[i] == -1:
                size1 = i-0+1
            else:
                size1 = i - left_s[i]
            if right_s[i] == -1:
                size2 = n - i
            else:
                size2 = right_s[i] - i
            min_c += A[i] * size2 * size1
        return max_c-min_c



if __name__ == '__main__':
    A = [1, 2, 2]
    s = Solution()
    ans = s.solve(A)
    print(ans)




