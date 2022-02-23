class Solution:
    def removeBrackets(self, Exp):
        # code here
        char = []
        opr = []
        ans = []
        hash_map = {'+': 1, '-': 1, '*': 2, '/': 2}
        for i in Exp:
            if i in hash_map or i == '(' or i == ')':
                opr.append(i)
            else:
                char.append(i)
        i = 0
        while i < len(opr):
            if (opr[i] == '(' or opr[i] == ')') and i > 0 and i < len(opr) - 1:
                if hash_map[opr[i - 1]] == hash_map[opr[i - 1]]:
                    opr.pop(i)
                if opr[i] == '(' and opr[i + 1] == ')':
                    opr.pop(i)
                    opr.pop(i + 1)
            i += 1
        for i in Exp:
            if i in hash_map or i == '(' or i == ')':
                if i == opr[0]:
                    opr.pop(0)
                    ans.append(i)
            else:
                ans.append(i)
        if ans[0] == '(' and ans[-1] == ')':
            ans.pop(0)
            ans.pop()
        return ''.join(ans)

# {
#  Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = 1
    for _ in range(t):
        Exp = input()

        ob = Solution()
        print(ob.removeBrackets(Exp))

# } Driver Code Ends