class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        ans = ''
        s = {'a', 'e', 'i', 'o', 'u'}
        for i in A:
            if i in s:
                ans += '#'
            elif ord(i) >= ord('b') and ord(i) <= ord('z'):
                ans += i
        return ans


if __name__ == '__main__':
    A = 'hgUe'
    
    s = Solution()
    print(s.solve(A))




