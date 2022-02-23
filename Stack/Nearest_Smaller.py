def prevSmaller(A):
    stack = []
    lst = []
    for i in range(len(A)):
        ans = -1
        while len(stack) > 0:
            if stack[-1] >= A[i]:
                stack.pop()
            elif stack[-1] < A[i]:
                ans = stack[-1]
                break
        lst.append(ans)
        stack.append(A[i])
    return lst

def largestRectangleArea( A):
    start = 0
    n = len(A)
    i = 0
    max_area = 0
    while i < n:
        width = i - start + 1
        min_val = min(A[start:start + width])
        area = width * min_val
        if area > max_area:
            max_area = area
            i += 1
        else:
            if start < i:
                start += 1
            else:
                start += 1
                i += 1
    return max_area

if __name__ == "__main__":
    A = [39, 27, 11, 4, 24, 32, 32, 1]
    print(prevSmaller(A))
    B = [6, 2, 5, 4, 5, 1, 6]
    print(largestRectangleArea(B))

