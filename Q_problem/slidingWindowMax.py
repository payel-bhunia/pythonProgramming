class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        cl = []
        ans = []
        if B == 1:
            return A
        for i in range(B):
            if len(cl) > 0:
                if A[i] > cl[0]:
                    cl = []
                else:
                    while A[i] > cl[-1]:
                        cl.pop()
            cl.append(A[i])
        ans.append(cl[0])
        end = B
        start = 0
        while end < len(A):
            if A[start] == ans[start]:
                cl.pop(0)
            start += 1
            if A[end] > cl[0]:
                cl = []
            else:
                if len(cl) > 0:
                    while A[end] > cl[-1]:
                        cl.pop()
            cl.append(A[end])
            ans.append(cl[0])
            end += 1
        return ans

if __name__ == '__main__':
    A = [90, 943, 777, 658, 742, 559, 623, 263, 880, 176, 354, 434, 699, 501, 551, 821, 563, 974, 701, 479, 238, 87, 61, 910, 204, 534, 369, 845, 566, 19, 939, 87, 708, 323, 662, 32, 655, 835, 67, 360, 550, 173, 488, 420, 680, 805, 630, 48, 791, 991, 791, 819, 772, 228, 123, 303, 642, 780, 115, 89, 919, 830, 271, 853, 588, 249, 20, 940, 851, 749, 340, 587, 235, 106, 125, 32, 319, 590, 354, 751, 761, 564, 484, 51, 202, 370, 216, 130, 146, 632]
    B = 6
    s = Solution()
    ans = s.slidingMaximum(A, B)
    print(ans)



