class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.sorted = None

    def insertion_sort(self):
        ref = self.head
        while ref is not None:
            self.sort_list(ref.data)
            ref = ref.next
        self.printlist(self.sorted)

    def printlist(self, head_name):
        ref = head_name
        while ref.next is not None:
            print(ref.data, '-->', end="")
            ref = ref.next
        if ref is not None:
            print(ref.data)

    def push_data(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            ref = self.head
            while ref.next is not None:
                ref = ref.next
            ref.next = Node(data)

    def sort_list(self, data):
        # print(data)
        node = Node(data)
        if self.sorted is None:
            self.sorted = node
        elif self.sorted.data > data:
            node.next = self.sorted
            self.sorted = node
        else:
            ref = self.sorted
            prev = ref
            ref = ref.next
            while ref.data < data and ref.next is not None:
                prev = ref
                ref = ref.next
            prev.next = node
            node.next = ref




if __name__ == "__main__":
    llist = LinkedList()
    llist.push_data(30)
    llist.push_data(3)
    llist.push_data(4)
    llist.push_data(20)
    llist.push_data(5)
    llist.printlist(llist.head)
    llist.insertion_sort()








