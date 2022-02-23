def gen(visited,curr,ans,idx,B,A,count):
    #base
    if count == B:
        ans.append(curr)
        return

    for i in range(idx,A):
        if visited[i] == 0:
            visited[i]=1
            curr.append(i+1)
            gen(visited.copy(),curr.copy(),ans,i+1,B,A,count+1)
            visited[i]=0
            curr.pop()

class Solution:
    def combine(self, A, B):
        curr = []
        ans = []
        idx = 0
        visited = [0] * A
        count = 0
        gen(visited, curr, ans, idx, B, A,count)
        return ans



if __name__ == '__main__':
    A = 10
    B = 9
    s = Solution()
    ans = s.combine(A,B)
    print(ans)
