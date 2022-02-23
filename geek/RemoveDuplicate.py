# User function template for Python

class Solution:
    def remove_duplicate(self, A, N):
        print(A)
        if N <= 1:
            return A
        i = 0
        j = 1
        while j < len(A):
            if A[i] == A[j]:
                A.pop(j)
            else:
                i = j
                j += 1
        #print(A)
        return len(A)


        # code here


# {
#  Driver Code Starts
# Initial template for Python

if __name__ == '__main__':
    t = 1
    for i in range(t):
        N = 5
        A = [4,9,9,1,1,5]
        ob = Solution()
        n = ob.remove_duplicate(A, N)
        for i in range(n):
            print(A[i], end=" ")
        print()

# } Driver Code Ends

