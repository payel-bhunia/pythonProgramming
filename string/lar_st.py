class Solution:
    def getLargest(self, A):
        T = []
        for i in range(len(A)):
            if A[i] == '_':
                T[:0] = A[i + 1:]
                end = i + 1
                break
        T.sort(reverse=True)
        ans = ''
        n = len(T)
        start = 0
        for i in range(end - 1):
            if start < n:
                if ord(A[i]) < ord(T[start]):
                    ans += T[start]
                    start += 1
                else:
                    ans += A[i]
            else:
                ans += A[i:end - 1]
                break
        return ans


A = 'abb_c'
s = Solution()
print(s.getLargest(A))



