class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        hashmap = dict()
        start = 0
        end = 0
        count = 0
        mod = 1000000007
        size = 0
        c = 0
        while end < n:
            if A[end] not in hashmap:
                hashmap[A[end]] = end
                size += 1
            else:
                if hashmap[A[end]] >= start:
                    start = hashmap[A[end]]+1
                    hashmap[A[end]] = end
                    size = end - start + 1
                else:
                    del hashmap[A[end]]
                    continue

            c += size
            print(A[start:end + 1], size,c)
            count = (count+size) % mod
            end += 1

        return count


if __name__ == '__main__':
    A = [79, 78, 46, 36, 51, 56, 84, 85, 4, 26, 38, 23, 76, 62, 98, 41, 8, 79, 98, 84, 81, 14, 77]
    s = Solution()
    ans = s.solve(A)
    print(ans)