class LinkedList:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Head:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        self.cachelimit = 4


class LRU_cache:
    def __init__(self):
        self.cacheMap = {}
        self.start = None

    def push(self,val):
        if self.start is None:
            node = LinkedList(val)
            h = Head()
            h.head = node
            h.tail = node
            h.size = 1
            self.start = h
            self.cacheMap[val] = node
        else:
            h = self.start
            if val not in self.cacheMap:
                node = LinkedList(val)
                if h.size == h.cachelimit:
                    deleted = h.head
                    print('deleted', deleted.val)
                    h.head = h.head.right
                    h.head.left = None
                    del self.cacheMap[deleted.val]
                    h.size -= 1
                h.tail.right = node
                node.left = h.tail
                h.tail = node
                self.cacheMap[val] = node
                h.size += 1
            else:
                node = self.cacheMap[val]
                if h.head != node:
                    prev = node.left
                    nxt = node.right
                    prev.right = nxt
                    nxt.left = prev
                else:
                    h.head = h.head.right
                    h.head.left = None
                h.tail.right = node
                node.left = h.tail
                node.right = None
                h.tail = node

    def get(self, val):
        h = self.start
        if val in self.cacheMap:
            node = self.cacheMap[val]
            if h.head != node:
                prev = node.left
                nxt = node.right
                prev.right = nxt
                nxt.left = prev
            else:
                h.head = h.head.right
                h.head.left = None
            h.tail.right = node
            node.left = h.tail
            node.right = None
            h.tail = node
            return 1
        else:
            self.push(val)
            return -1

    def traverse(self):
        h = self.start
        curr = h.head
        while curr != None:
            if curr.right == None:
                print(curr.val,end="")
            else:
                print(curr.val, '-->', end="")
            curr = curr.right
        print(" ")

if __name__ == "__main__":
    lru = LRU_cache()
    A = [['put', 1], ['put', 2], ['put', 3], ['get', 4], ['get', 2], ['get', 1],['get', 6],['get', 7],['get', 9]]
    ans = []
    for i in A:
        if i[0] == 'put':
            lru.push(i[1])
            print("After pushing element", i[1], ' cache looks like ')
            lru.traverse()
            ans.append('null')
        else:
            isPresent = lru.get(i[1])
            print("For searching element", i[1], ' result is ', isPresent,)
            print('now cache looks like ')
            ans.append(isPresent)
            lru.traverse()
    print('final result is ', ans)







