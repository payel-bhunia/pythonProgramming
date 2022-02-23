# Your task is to complete this function
# Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        # Code here
        max_size = 0
        pref = [0] * n
        pref[0] = arr[0]
        hash_map = {}
        hash_map[pref[0]] = [0, 0]
        for i in range(1, n):
            pref[i] = pref[i - 1] + arr[i]
            if pref[i] in hash_map:
                hash_map[pref[i]][1] = i
                max_size = max(max_size, hash_map[pref[i]][1] - hash_map[pref[i]][0])
            else:
                hash_map[pref[i]] = [i, i]
            if pref[i] == 0:
                max_size = max(max_size, i + 1)
        #print(hash_map)
        #print(pref[0],pref[1],pref[3609],pref[3608])
        for key, value in hash_map.items():
            max_size = max(max_size, value[1] - value[0])
        return max_size


# {
#  Driver Code Starts
if __name__ == '__main__':
    t = 1
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        ob = Solution()
        print(ob.maxLen(n, arr))
# Contributed by: Harshit Sidhwa
# } Driver Code Ends