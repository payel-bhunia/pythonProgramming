class Solution:
    def singleElement(self, arr):
        # code here
        ans = 0
        for i in range(32):
            count1 = 0
            for j in arr:
                if (j>>i)&1 == 1:
                    count1 += 1
            bit = count1%3
            print("count of 1: ", count1, "bit= ", bit)
            if bit == 1 and i != 31:
                ans += (1<<i)
                print(ans)
            if bit == 1 and i == 31:
                ans = ans * (-1)
        return ans


s = Solution()
A = [-10]
print(s.singleElement(A))