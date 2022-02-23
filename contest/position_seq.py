class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A * (A + 1) // 2 == B:
            return 0
        ans = []
        n = A
        summ = B
        ans.append(1)
        n = n - 1
        B = B - 1
        prev = 1
        i = 0
        count = 0
        while n > 0:
            if B // n == prev + 1 and B % n == 0:
                while n > 0:
                    ans.append(prev + 1)
                    i+=1
                    n -= 1
                    if ans[i] != i + 1:
                        count += 1
                break
            elif B // n >= prev + 1:
                ans.append(prev + 1)
                i+=1
                prev += 1
            else:
                ans.append(prev)
                i +=1
            n -= 1
            B -= prev
            if ans[i] != i+1:
                count +=1
        print(ans)
        return count


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if A * (A + 1) // 2 == B:
            return 0
        ans = []
        n = A
        summ = B
        ans.append(1)
        n = n - 1
        B = B - 1
        prev = 1
        count = 0
        i = 0
        while n > 0:
            if B // n == prev + 1 and B % n == 0:
                while n > 0:
                    ans.append(prev + 1)
                    i += 1
                    n -= 1
                    if ans[i] != i + 1:
                        count += 1
                break
            elif B // n >= prev + 1:
                ans.append(prev + 1)
                i += 1
                prev += 1
            else:
                ans.append(prev)
                i += 1
            n -= 1
            B -= prev
            if ans[i] != i + 1:
                count += 1

        return count


if __name__ == '__main__':
    tc = 1
    while tc > 0:
        A = 2
        B = 2
        ob = Solution()
        ans = ob.solve(A,B)
        print(ans)
        tc -= 1