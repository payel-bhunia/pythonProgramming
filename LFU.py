from collections import OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = OrderedDict()
        self.hash_freq = dict()
        self.freq_count = {}
        self.least_freq = 0

    def check_tie(self, key, least_freq_key) -> int:
        l = list(self.hash_map.items())
        for i in range(len(l)):
            if l[i][0] == key:
                index_key = i
            elif l[i][0] == least_freq_key:
                min_index = i
        if index_key > min_index:
            return least_freq_key
        else:
            return key

    def get(self, key: int) -> int:
        value = -1
        if key in self.hash_map:
            value = self.hash_map[key]
            self.hash_map.pop(key)
            self.hash_map[key] = value
            self.hash_freq[key] += 1
        return value

    def put(self, key: int, value: int) -> None:
        main_key = key
        if main_key in self.hash_map:
            self.hash_map.pop(main_key)
            self.hash_map[main_key] = value
            self.hash_freq[main_key] += 1

        else:

            if len(self.hash_map) == self.capacity:
                least_freq = 10 ** 9
                least_freq_key = main_key
                for key in self.hash_freq:
                    if self.hash_freq[key] < least_freq:
                        least_freq = self.hash_freq[key]
                        least_freq_key = key
                    elif self.hash_freq[key] == least_freq:
                        print('before tie', key, least_freq_key)
                        least_freq_key = self.check_tie(key, least_freq_key)
                        print(least_freq_key)
                if len(self.hash_map) > 0:
                    self.hash_map.pop(least_freq_key)
                    self.hash_freq.pop(least_freq_key)
            self.hash_map[main_key] = value
            self.hash_freq[main_key] = 1
            print(self.hash_map, 'for put[', main_key, value, ']')
            print(self.hash_freq)

#A = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get", "put", "put","get", "put","get"]
#B = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4], [4, 4], [3, 3], [2], [2,2], [2]]
A = ["LFUCache","put","get"]
B = [[0],[0,0],[0]]
n = len(A)
print(A)
print(B)
print(n)
A[0] = LFUCache(B[0][0])
ans = []
ans.append("null")

for i in range(1, n):
    if A[i] == "put":
        key = B[i][0]
        value = B[i][1]
        A[0].put(key, value)
        ans.append("null")
    else:
        key = B[i][0]
        ans.append(A[0].get(key))
print(ans)



