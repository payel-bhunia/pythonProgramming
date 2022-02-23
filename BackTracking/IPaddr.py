def gen(s, ans, curr, n, start, end, count):
    # base
    if start == end and end == n:
        if count == 4:
            ans.append('.'.join(curr))
            return
        else:
            return

    if start > n or end > n:
        return
    if int(s[start:end + 1]) >= 0 and int(s[start:end + 1]) <= 255:
        if int(s[start:end + 1]) == 0 and end - start + 1 > 1:
            return
        elif int(s[start:end + 1]) > 0 and int(s[start:end + 1]) <= 9 and end - start + 1 > 1:
            return
        else:
            curr.append(s[start:end + 1])
            gen(s, ans, curr.copy(), n, end + 1, end + 1, count + 1)
            curr.pop()
            gen(s, ans, curr.copy(), n, start, end + 1, count)


def generateIPAddress(s):
    # Write your code here.
    ans = []
    curr = []
    if len(s) < 4:
        return []
    elif len(s) == 4:
        # print('.'.join(list(s)))
        ans.append('.'.join(list(s)))
        return ans
    else:
        start = 0
        end = 0
        gen(s, ans, curr, len(s), start, end, 0)
        return ans


if __name__ == "__main__":
    s = '023579'
    #print(s)
    #print('.'.join(s))

    ans = generateIPAddress(s)
    print(ans)


    1688517
    umesh.prasad1@tcs.com
