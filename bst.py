# Binary Search Tree operations in Python


# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node is not None:
        # Traverse left
        inorder(node.left)

        # Traverse root
        print(str(node.data) + "->", end=' ')

        # Traverse right
        inorder(node.right)





def insert(node, value):
    if node is None:
        return Node(value)

    if(value>node.data):
        node.right = insert(node.right, value)
    else:
        node.left = insert(node.left, value)

    return node

# Find the inorder successor
def minValueNode(node):
    current = node

    # Find the leftmost leaf
    while(current.left is not None):
        current = current.left

    return current


# Deleting a node
def deleteNode(node, value):

    # Return if the tree is empty
    if node is None:
        return value

    # Find the node to be deleted
    if value < node.data:
        node.left = deleteNode(node.left, value)
    elif(value > node.data):
        node.right = deleteNode(node.right, value)
    else:
        # If the node is with only one child or no child
        if node.left is None:
            temp = node.right
            root = None
            return temp

        elif node.right is None:
            temp = node.left
            root = None
            return temp

        # If the node has two children,
        # place the inorder successor in position of the node to be deleted
        temp = minValueNode(node.right)

        node.data = temp.data

        # Delete the inorder successor
        node.right = deleteNode(node.right, temp.data)

    return node



def printt(node):
    if node is None:
        return
    else:
        print(node.data)
        printt(node.left)
        printt(node.right)


def height(root):
    # Check if the binary tree is empty
    if root is None:
        # If TRUE return 0
        return 0
        # Recursively call height of each node
    leftAns = height(root.left)
    rightAns = height(root.right)

    # Return max(leftHeight, rightHeight) at each iteration
    return max(leftAns, rightAns) + 1

def get_level(node, data, level=0):
    print(type(data))
    if node.data == data:
        return level
    if data < node.data:
        if node.left:
            return get_level(node.left,data,level+1)
    else:
        if node.right:
            return get_level(node.right,data,level+1)

    return level



