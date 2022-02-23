from collections import deque
class Solutions:
    def solve(self,A, B):
        n = len(A)
        count_B = B
        start = 0
        start0 = -1
        end = 0
        size = 0
        max_len = -1000000007
        cl = deque()
        left = -1
        right = -1
        while end < n:
            if A[end] == 0:
                if count_B == 0:
                    size = size - (start0 - start + 1)
                    start = cl[0] + 1
                    cl.popleft()
                    if len(cl) > 0:
                        start0 = cl[0]
                    else:
                        start0 = end
                else:
                    if start0 == -1:
                        start0 = end
                        if start == -1:
                            start = end
                    count_B -= 1
                cl.append(end)
            size += 1
            end += 1
            if size > max_len:
                max_len = size
                left = start
                right = end
        l = list(range(left, right, 1))
        return l


if __name__ == "__main__":
    A = [1, 1, 0, 0, 1, 0, 1, 1, 1]
    C = 2
    s = Solutions()
    print(s.solve(A, C))

