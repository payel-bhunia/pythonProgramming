# your task is to complete this function
# function should return index to the any valid peak element
class Solution:
    def peakElement(self, arr, n):
        if n > 1:
            if arr[1] < arr[0]:
                return 0
            if arr[-1] > arr[-2]:
                return n - 1
            low = 0
            high = n - 1
            while low <= high:
                mid = low + (high - low) // 2
                if mid > 0 and mid < n - 1:
                    if arr[mid] >= arr[mid - 1] and arr[mid] >= arr[mid + 1]:
                        return mid
                    elif arr[mid] >= arr[mid + 1]:
                        res = mid
                        high = mid - 1
                    else:
                        low = mid + 1
            if low > high:
                if arr[low] >= arr[low - 1] and arr[low] >= arr[low + 1]:
                    return low
                elif arr[high] >= arr[high - 1] and arr[high] >= arr[high + 1]:
                    return high
                else:
                    return -1

        # Code here


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = 1
    for i in range(t):
        n = 6
        arr = [4,7,2,3,9,5]
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] >= arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] >= arr[index - 1]:
                flag = True
            elif arr[index - 1] <= arr[index] and arr[index] >= arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends