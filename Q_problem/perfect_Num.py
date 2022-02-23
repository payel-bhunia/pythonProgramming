from collections import deque

class Solution:
    # @param A : integer
    # @return a strings
    def solve(self, A):
        deq = deque(['1','2'])
        ans = []
        count = 0
        while count < A:
            ele = deq[0]
            ans.append(ele+ele[::-1])
            count += 1
            if count == A:
                return ele
            else:
                deq.append(ele + '1')
                deq.append(ele + '2')
                deq.popleft()


if __name__ == '__main__':
    A = 10
    s = Solution()
    ans = s.solve(A)
    print(ans)









