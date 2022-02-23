class Solution:
    def solve(self, s):
        alpha_list = {}
        for i in range(26):
            char = chr(ord('A')+i)
            alpha_list[char] = i+1
        n = len(s)-1
        val = 0
        for i in s:
            val += alpha_list[i] * (26 ** n)
            n -= 1

        return val


if __name__ == '__main__':
    #t = int(input())
    #for _ in range(t):
    #    S = input()
    s = 'AB'
    ob = Solution()
    print(ob.solve(s))
