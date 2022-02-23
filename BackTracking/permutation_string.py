def gen(str, hash_map, curr, ans, idx, n):
    # base
    if idx == n:
        ans.append(''.join(curr))
        return

    for i in hash_map:
        if hash_map[i] > 0:
            hash_map[i] -= 1
            curr.append(i)
            gen(str, hash_map.copy(), curr.copy(), ans, idx + 1, n)
            hash_map[i] += 1
            curr.pop()


def uniquePrem(str):
    # Write your code here.
    #str.sort()
    A = []
    for i in str:
        A.append(i)
    A.sort()
    str1 = ''.join(A)
    hash_map = {}
    for i in str:
        if i in hash_map:
            hash_map[i] += 1
        else:
            hash_map[i] = 1
    curr = []
    ans = []
    n = len(str)
    idx = 0
    gen(str1, hash_map, curr, ans, idx, n)
    return ans

if __name__ == '__main__':
    A = ['a', 'b', 'c']
    print(type(''.join(A)))
    print('0'*3)
    ans = uniquePrem(A)
    print(ans)