import create


def binarysearch(root, val):
    if root.data > val:
        if root.left:
            binarysearch(root.left , val)
        else:
            print(val, "Not found")
    elif root.data < val:
        if root.right:
            binarysearch(root.right, val)
        else:
            print(val, "Not found")
    else:
        print(val, "Finally found!")


if __name__ == "__main__":
    root = create.Node(10)
    root.insert_node(11)
    root.insert_node(4)
    root.insert_node(7)
    root.insert_node(6)
    root.insert_node(12)
    binarysearch(root, 5)
    binarysearch(root, 4)
    binarysearch(root, 11)
