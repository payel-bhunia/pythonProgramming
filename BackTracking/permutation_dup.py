def gen(A, hash_map, ans, curr, idx,n):
    if idx == n:
        ans.append(curr)
        return ans
    #base
    for i in hash_map:
        if hash_map[i] > 0:
            curr.append(i)
            hash_map[i] -= 1
            gen(A, hash_map.copy(), ans, curr.copy(), idx+1, n)
            curr.pop()
            hash_map[i] += 1



class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        n = len(A)
        hash_map ={}
        for i in A:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        idx = 0
        ans = []
        curr = []
        gen(A, hash_map, ans, curr, idx,n)
        return ans

if __name__ == '__main__':
    A = [3,2,3]
    s = Solution()
    ans = s.permute(A)
    print(ans)