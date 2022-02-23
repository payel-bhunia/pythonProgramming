

def subset(A,ans, lst, ind):
    ans.append(lst)
    if ind == len(A):
        return 
    for i in range(ind,len(A)):
        lst1 = lst.copy()
        lst1[ind] = 1
        subset(A, ans, lst1,ind+1)


class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        ans = []
        ind = 0
        lst = [0]*len(A)
        subset(A, ans, lst, ind)
        #ans.sort()
        print(ans)


if __name__ == '__main__':
    A = [1,2,3]
    s = Solution()
    ans = s.subsets(A)
    print(ans)

