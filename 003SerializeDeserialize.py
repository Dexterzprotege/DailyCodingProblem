# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree
# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
# You may serialize the following tree:

#     1
#    / \
#   2   3
#      / \
#     4   5
# as "[1,2,3,null,null,4,5]"
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def serialize(root):
    q = deque()
    q.append(root)
    result = []
    while q:
        node = q.popleft()
        if not node:
            result.append("null")
            continue
        else:
            result.append(node.val)
        q.append(node.left)
        q.append(node.right)
    return result

def deserialize(data):
    if not data or data[0] == 'null': return None
    q = deque()
    root = Node(int(data[0]))
    q.append(root)
    i = 1
    while q and i < len(data):
        node = q.popleft()
        if data[i] != 'null':
            node.left = Node(int(data[i]))
            q.append(node.left)
        i += 1
        if data[i] != 'null':
            node.right = Node(data[i])
            q.append(node.right)
        i += 1
    return root
root=Node(10)
root.left=Node(16)
root.right=Node(14)
root.left.left=Node(4)
root.left.right=Node(8)
root.right.left=Node(2)
root.right.right=Node(7)
ans=serialize(root)
print(ans)
print(deserialize(ans).val)



