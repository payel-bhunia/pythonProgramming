class Node:
    def __init__(self, data_val):
        self.data = data_val
        self.next = None


class SingleLlist:
    def __init__(self):
        self.head = None

    def traverse(self):
        head = self.head
        while head != None:
            print(head.data)
            head = head.next

    def insert_begin(self,node):
        n1 = self.head
        self.head = node
        self.head.next = n1

    def insert_end(self, node):
        h = self.head
        if h == None:
            self.head = node
        else:
            while h.next != None:
                h = h.next
            h.next = node

    def insert_mid(self, node, pos):
        head = self.head
        count = 1
        while head.next != None:
            if count == pos:
                break
            else:
                head = head.next
                count += 1
        node2 = head.next
        head.next = node
        node.next = node2

    def remove_item(self,val):
        head = self.head
        prev_node = head
        found = 0
        if head.data == val:
            self.head = self.head.next
            return 1
        else:
            prev_node = head
            head = head.next
            while head != None:
                if head.data == val:
                    found = 1
                    break
                else:
                    prev_node = head
                    head = head.next
            if found == 1:
                prev_node.next = head.next
                return 1
            else:
                return 0

    def get_middle(self):
        slow = self.head
        fast = self.head
        print(slow.data)
        print(fast.data)
        if self.head:
            while fast != None:# or fast.next != None:
                fast = fast.next.next
                slow = slow.next
        return slow




if __name__ == "__main__":
    ob1 = SingleLlist()
    l = ["A", "B", "C", "D", "E"]
    e1 = Node(l[0])
    ob1.head = e1
    for i in range(1, len(l)):
        e = Node(l[i])
        e1.next = e
        e1 = e
    ob1.traverse()
    new_Node = Node("X")
    ob1.insert_begin(new_Node)
    print("-----")
    ob1.traverse()
    new_Node = Node("Z")
    ob1.insert_end(new_Node)
    print("-----")
    ob1.traverse()
    ob2 = SingleLlist()
    new_Node = Node("P")
    ob2.insert_end(new_Node)
    print("-----")
    ob2.traverse()
    new_Node = Node("N")
    ob1.insert_mid(new_Node, 12)
    print("-----")
    ob1.traverse()
    val = ob1.remove_item("V")
    if val == 1:
        print("deleted")
    else:
        print("not found")
    ob1.traverse()
    node = ob1.get_middle()
    print("Middle-- :", node.data)
    print('------ob2-----')
    ob2.traverse()







