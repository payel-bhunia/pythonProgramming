def check_sq(val):
    start = 0
    end = val // 2
    while start <= end:
        mid = start + (end - start) // 2
        if mid * mid > val:
            end = mid - 1
        elif mid * mid < val:
            start = mid + 1
        else:
            return True
    return False


def gen(hash_map,n,count,ans,last,curr):
    if count == n:
        ans[0] += 1
        return
    for i in hash_map:
        if hash_map[i] > 0:
            if last != 1000000007:
                if check_sq(i+last):
                    hash_map[i] -= 1
                    temp = last
                    last = i
                    count += 1
                    curr.append(i)
                    gen(hash_map.copy(), n, count, ans, last,curr.copy())
                    hash_map[i] += 1
                    last = temp
                    count -= 1
                    curr.pop()
            else:
                hash_map[i] -= 1
                temp = last
                last = i
                count += 1
                curr.append(i)
                gen(hash_map.copy(), n, count, ans, last,curr.copy())
                hash_map[i] += 1
                last = temp
                count -= 1
                curr.pop()


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def solve(self, A):
        n = len(A)
        hash_map = {}
        for i in A:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
        ans = [0]
        last = 1000000007
        curr = []
        gen(hash_map,n,0,ans,last,curr)
        return ans[0]

if __name__ == '__main__':
    A = []
    s = Solution()
    ans = s.solve(A)
    print(ans)