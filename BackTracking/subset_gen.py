

def subset(A,ans, lst, ind):
    if ind == len(A):
        ans.append(lst)
        return
    lst.append(A[ind])
    subset(A,ans, lst.copy(),ind+1)
    lst.pop()
    subset(A,ans, lst.copy(),ind+1)



class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        ans = []
        ind = 0
        lst = []
        subset(A, ans, lst, ind)
        #ans.sort()
        print(ans)


if __name__ == '__main__':
    A = [1,2,3]
    s = Solution()
    ans = s.subsets(A)
    print(ans)

