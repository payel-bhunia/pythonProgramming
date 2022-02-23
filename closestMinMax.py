class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        max_val = -10 ** 9
        min_val = 10 ** 9
        start = 0
        end = 0
        flag_min = 0
        flag_max = 0
        for i in range(n):
            if A[i] < min_val:
                min_val = A[i]
            if A[i] > max_val:
                max_val = A[i]
        if min_val == max_val:
            return 1
        else:
            min_size = 10**9
            for i in range(n):
                if A[i] == max_val:
                    if flag_max == 0:
                        if flag_min == 0:
                            start = i
                            flag_max = 1
                        else:
                            end = i
                            min_size = min(min_size, (end - start + 1))
                            start = i
                            flag_min = 0
                            flag_max = 1
                    else:
                        start = i
                elif A[i] == min_val:
                    if flag_min == 0:
                        if flag_max == 0:
                            start = i
                            flag_min = 1
                        else:
                            end = i
                            min_size = min(min_size, (end - start + 1))
                            start = i
                            flag_max = 0
                            flag_min = 1
                    else:
                        start = i
            return min_size


if __name__ == '__main__':
    A = [1, 2, 3, 3, 1, 1]
    s= Solution()
    n = s.solve(A)
    print(n)