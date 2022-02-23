class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        total = sum(B)
        each_sum = total//3
        p1_sum = 0
        p1_list=[]
        p2_list = []
        count=0
        p1_cnt=0
        p2_cnt=0
        for i in range(A-2):
            p1_sum += B[i]
            if p1_sum == each_sum:
                p1_list.append(i)
                p1_cnt += 1
        for i in range(p1_cnt):
            start = p1_list[i] + 1
            p2_sum = 0
            for j in range(start, A-1):
                p2_sum += B[j]
                if p2_sum == each_sum:
                    p2_cnt += 1
                    p2_list.append(j)
        for i in range(p2_cnt):
            start = p2_list[i] + 1
            p3_sum = sum(B[start:])
            if p3_sum == each_sum:
                count += 1
        return count




if __name__ == '__main__':
    S = 5
    A = [1, 1, 1, 1, 1 ]
    ob = Solution()
    print(ob.solve(S, A))

