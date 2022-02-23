def gen( B, result, temp, idx):
    if idx == len(temp) and len(temp) > 0:
        staging = []
        for i in range(len(temp)):
            if temp[i] > 0:
                staging += [B[i].val] * temp[i]
        result.append(staging)
        return
    for i in range(B[idx].freq + 1):
        temp1 = temp.copy()
        temp1[idx] = i
        gen(B, result, temp1, idx + 1)


class frequency:
    def __init__(self, val, freq):
        self.val = val
        self.freq = freq


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        B = []
        hashmap = {}
        C = []
        for i in A:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
        for i in hashmap:
            obj = frequency(i, hashmap[i])
            B.append(obj)
            C.append(i)
        result = []
        #print(C)
        temp = [0]*len(B)
        idx = 0
        if len(B) > 0:
            gen(B, result, temp, idx)
            #result.sort()
        return result



if __name__ == '__main__':
    A = [1,2,2]
    s = Solution()
    ans = s.subsetsWithDup(A)
    ans.sort()
    print(ans)