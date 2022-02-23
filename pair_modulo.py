class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        summ = 0
        mod = 1000000007
        hash_map = {}
        arr = []
        for i in A:
            if i in hash_map:
                hash_map[i] += 1
            else:
                hash_map[i] = 1
                arr.append(i)
        n = len(arr)
        for i in range(n-1):
            for j in range(i+1 , n):
                if i != j:
                    print(hash_map,i,j)
                    summ = (summ +((arr[i] % arr[j]) + (arr[j] % arr[i]))) % mod
        return summ


if __name__ == '__main__':
    A = [794, 924, 452, 548, 78, 475, 836, 924, 426, 421, 548, 115, 480, 926, 519, 45, 464, 116, 356, 111, 79, 732, 309, 817, 880, 12, 119, 207, 433, 1, 947, 202, 95, 90, 468, 620, 996, 692, 178, 700, 311, 848, 742, 782, 933, 586, 7, 671, 872, 235, 92, 383, 637, 952, 507, 360, 705, 684, 618, 303, 334, 876, 500, 104, 491, 866, 966, 863, 498, 581, 554, 244, 223, 679, 892, 166, 877, 246, 699, 595, 794, 567, 282, 6, 862, 528, 936, 19, 64, 796, 212, 24, 714, 725, 749, 620, 862, 37, 90, 876]
    s = Solution()
    print(s.solve(A))
