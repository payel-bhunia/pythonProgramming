from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = OrderedDict()

    def get(self, key: int) -> int:
        value = -1
        if key in self.hash_map:
            value = self.hash_map[key]
            self.hash_map.pop(key)
            self.hash_map[key] = value
        return value

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map.pop(key)
        else:
            if len(self.hash_map) >= self.capacity:
                self.hash_map.popitem(last=False)
        self.hash_map[key] = value


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
A = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
B = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
n = len(A)
print(A)
print(B)
print(n)
A[0] = LRUCache(B[0][0])
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



