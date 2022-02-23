class Solution:
    def numDecodings(self, A):
        n = len(A)
        mod = 1000000007
        count = 0
        i = 0
        while i < n:
            if A[i] != '0':
                if A[i+1] != '0':
                    count += 1
                    i += 1
                else:
                    i += 2
            else:
                i += 1
        i = 0
        while i < n-1:
            if A[i] != '0':
                if int(A[i:i+2]) < 27:
                    count += 1
                else:
                    if A[i+1] == '0':
                        return 0
            i += 1

        return count


if __name__ == '__main__':
    A = '5163490394499093221199401898020270545859326357520618953580237168826696965537789565062429676962877038781708385575876312877941367557410101383684194057405018861234394660905712238428675120866930196204792703765204322329401298924190'
    s = Solution()
    print(s.numDecodings(A))

