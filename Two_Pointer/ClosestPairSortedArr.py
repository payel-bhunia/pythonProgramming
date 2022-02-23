class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : integer
    # @return a list of integers
    def solve(self, A, B, C):
        n = len(A)
        m = len(B)
        min_diff = 1000000007
        pair = [-1,-1]
        start1 = 0
        start2 = m-1
        while start1 < n and start2 >= 0:
            diff = abs(A[start1]+B[start2]-C)
            diff_left = abs(A[start1]+B[start2-1]-C)
            diff_right = abs(A[start1] + B[start2 + 1] - C)
            if diff > diff_left:
                diff = diff_left
                start2 = start2 - 1
            if diff > diff_right:
                diff = diff_right
                start2 = start2 + 1
            if diff < min_diff:
                min_diff = diff
                pair = [A[start1], B[start2]]
                if min_diff == 0:
                    return pair
            else:
                start1 += 1
        return pair

if __name__ == "__main__":
    A = [6, 7, 9, 13, 21, 29, 56, 74, 77, 83, 84, 88, 93, 96, 101, 104, 114, 115, 122, 125, 144, 147, 151, 152, 154, 161, 165, 167, 174, 179, 185, 189, 192, 194, 198, 201, 203, 208, 224, 229, 230, 238, 252, 253, 257, 264, 266, 275, 278, 279, 282, 284, 291, 312, 316, 322, 332, 335, 336, 339, 364, 380, 381, 384, 387, 388, 390, 392, 394, 395, 401, 403, 431, 432, 440, 442, 443, 444, 446, 451, 454, 461, 470, 483, 492]
    B = [2, 8, 13, 16, 19, 21, 22, 23, 37, 48, 63, 66, 68, 71, 72, 95, 102, 116, 123, 127, 131, 132, 146, 148, 153, 171, 173, 179, 187, 194, 215, 220, 227, 229, 240, 245, 254, 255, 257, 259, 271, 276, 277, 286, 296, 312, 314, 318, 321, 333, 339, 341, 343, 355, 356, 359, 363, 364, 380, 390, 393, 398, 401, 409, 413, 417, 427, 442, 444, 446, 454, 455, 459, 460, 468, 471, 473, 475, 476, 478, 479, 482, 483, 488, 489]
    C = 409
    s = Solution()
    print(s.solve(A, B, C))