class Solution:
    def solve(self, n):
        alpha_list = []
        for i in range(26):
            char = chr(ord('a')+i)
            alpha_list.append(char)
        val = ''
        while n > 0:
            n -= 1
            val = alpha_list[n % 26] + val
            n = n//26

        return val


if __name__ == '__main__':
    #t = int(input())
    #for _ in range(t):
    #    S = input()
    S = 52
    ob = Solution()
    print(ob.solve(S))
