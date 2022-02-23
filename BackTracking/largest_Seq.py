def check(curr, n):
    visited = [False] * n
    for i in range(n):
        if curr[i] != '1':
            if visited[i] == False:
                index = int(curr[i]) + i
                if index < n:
                    if curr[index] == curr[i]:
                        visited[i] = True
                        visited[index] = True
                    else:
                        return False
                else:
                    return False
        else:
            visited[i] = True
    return True


def gen(used, curr, ans, leng, n, idx):
    # base
    if idx == leng:
        #print(''.join(curr))
        if check(curr, leng):
            val = int(''.join(curr))
            ans[0] = max(ans[0],val)
            return
    for i in range(n):
        if used[i] > 0:
            curr.append(str(i + 1))
            used[i] -= 1
            gen(used.copy(), curr.copy(), ans, leng, n, idx + 1)
            curr.pop()
            used[i] += 1


def validSequence(n):
    # Write your code here.
    leng = 2 * n - 1
    curr = []
    ans = [-1000000007]
    used = [2] * n
    used[0] = 1
    idx = 0
    gen(used, curr, ans, leng, n, idx)
    return ans[0]


if __name__ == '__main__':
    A = 3
    
    ans = validSequence(A)
    print(ans)