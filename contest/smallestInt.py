class Solution:
    def smallestNumber(self, num: int) -> int:
        n = num
        digit= [0]*10
        state = 0
        if n > 0:
            state = 1
        else:
            n = n*(-1)
        while n > 0:
            digit[n%10] += 1
            n=n//10
        ans = ""
        if num > 0:
            flag = 0
            i = 1
            if digit[0] == 0:
                flag = 1
            while i < 10:
                if flag == 0 and digit[i] !=0:
                    ans += (str(i)*1)
                    ans += '0' * digit[0]
                    digit[i] -= 1
                    flag= 1
                    i -= 1
                elif flag == 1 and digit[i] !=0:
                    ans += (str(i)*digit[i])
                i += 1
            return int(ans)
        else:
            i = 9
            while i > -1:
                ans += (str(i)*digit[i])
                i -= 1
            return int(ans) * (-1)

s = Solution()
print(s.smallestNumber(5059))