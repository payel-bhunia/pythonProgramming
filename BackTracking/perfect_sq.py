def check_sq(val):
    start = 0
    end = val//2
    while start <= end:
        mid = start+(end-start)//2
        if mid * mid > val:
            end = mid-1
        elif mid * mid < val:
            start = mid+1
        else:
            return True
    return False

def gen(A, hash_map, ans, curr, idx,count,summ,i,n):
    if idx == n and count == 2:
        if check_sq(summ):
            print(curr)
            ans[0] += 1
            return
    if count == 2:
        if not check_sq(summ):
            return
        else:
            count = 0
            summ = i

    #base
    for i in hash_map:
        if hash_map[i] > 0:
            curr.append(i)
            hash_map[i] -= 1

            gen(A, hash_map.copy(), ans, curr.copy(), idx+1,count+1,summ+i,i, n)
            curr.pop()
            hash_map[i] += 1



class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        if n<=1:
            return 0
        hash_map ={}
        for i in A:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        idx = 0
        ans = [0]
        curr = []
        count =0
        summ =0
        last_val = 0
        gen(A, hash_map, ans, curr, idx,count,summ,last_val,n)
        return ans[0]

if __name__ == '__main__':
    A = [1,17,8]
    s = Solution()
    ans = s.solve(A)
    print(ans)