def subsetsUtil(A, subset, result, index):
    result.append(subset.copy())
    for i in range(index, len(A)):
        # include the A[i] in subset.
        subset.append(A[i])

        # move onto the next element.
        subsetsUtil(A, subset, result, i + 1)

        # exclude the A[i] from subset and
        # triggers backtracking.
        subset.pop(-1)
    return



# below function returns the subsets of vector A.
def subsets(A):
    global res
    subset = []
    result = []
    # keeps track of current element in vector A
    index = 0
    subsetsUtil(A, subset, result, index)
    print(result)


# Driver Code

# find the subsets of below vector.
array = [1, 2, 3]



# res will store all subsets.
# O(2 ^ (number of elements inside array))
# because at every step we have two choices
# either include or ignore.
subsets(array)