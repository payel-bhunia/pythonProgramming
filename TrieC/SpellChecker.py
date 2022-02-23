class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, st):
        n = len(st)
        for i in range(n):
            s = st[i]
            curr = self.root
            for c in s:
                index = ord(c) - ord('a')
                if curr.children[index] == None:
                    curr.children[index] = TrieNode()
                curr = curr.children[index]
            curr.isEnd = True

    def find(self, B):
        n = len(B)
        ans = []
        for i in range(n):
            flag = 1
            curr = self.root
            st = B[i]
            for s in st:
                index = ord(s) - ord('a')
                if curr.children[index] != None:
                    curr = curr.children[index]
                else:
                    flag = 0
                    break
            if flag == 1 and curr.isEnd == True:
                ans.append(1)
            else:
                ans.append(0)
        return ans


class Solution:
    # @param A : list of strings
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        t1 = Trie()
        t1.insert(A)
        ans = t1.find(B)
        return ans

if __name__ == "__main__":
    A = ['cat','cow', 'catsanddog','dog']
    B = ['cat','cowdung', 'catsanddog','doggy']
    s = Solution()
    ans = s.solve(A,B)
    print(ans)