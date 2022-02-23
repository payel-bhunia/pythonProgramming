class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusone(self, A):
        n = len(A)
        i = n-1
        carry = 0
        while i >= 0:
            if carry == 0:
                if i == n-1:
                    if A[i] != 9:
                        #print('here')
                        A[i]=A[i]+1
                        #print(i,A[i])
                        carry = 0
                    else :
                        A[i] = 0
                        carry = 1
                else:
                    break

            else:
                if A[i] != 9:
                    A[i] = A[i]+1
                    carry = 0
                else:
                    A[i] = 0
                    carry = 1
            i -= 1
        return A


def main():
    A = [1, 4, 5, 8, 9]
    s = Solution()
    n = s.plusone(A)
    print(n)


if __name__ == '__main__':
    main()
