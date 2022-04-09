class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.pos = []


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, st):
        n = len(st)
        for i in range(n):
            curr = self.root
            s = st[i]
            for c in s:
                index = ord(c) - ord('a')
                if curr.child[index] == None:
                    curr.child[index] = TrieNode()
                curr = curr.child[index]
                curr.pos.append(i)

    def find_path(self, B, final, A):
        for st in B:
            ans = ''
            curr = self.root
            flag = 1
            for j in st:
                index = ord(j) - ord('a')
                if curr.child[index] is None:
                    flag = 0
                    break
                else:
                    curr = curr.child[index]
            if flag == 1:
                n = len(curr.pos)
                if len(curr.pos) > 5:
                    n = 5
                for i in range(n):
                    if i == 0:
                        ans = A[curr.pos[i]]
                    else:
                        ans = ans + ' ' + A[curr.pos[i]]
            else:
                ans = '-1'
            final.append(ans)


def solve(n, A, W, B):
    W_sort = sorted(W, reverse=True)
    hash_map = {}

    for i in range(n):
        hash_map[W[i]] = A[i]
    j = 0
    for i in W_sort:
        A[j] = hash_map[i]
        j += 1
    trie = Trie()
    trie.insert(A)
    final = []
    trie.find_path(B, final, A)
    for i in final:
        print(i)


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    t = int(input())
    inp = []
    for i in range(t):
        size = list(map(int, input().split()))
        n, m = size[0], size[1]
        A = list(map(str, input().split()))
        W = list(map(int, input().split()))
        B = list(map(str, input().split()))
        inp.append([n, m, A, W, B])
    for i in range(t):
        solve(inp[i][0], inp[i][2], inp[i][3], inp[i][4])


if __name__ == '__main__':
    main()
