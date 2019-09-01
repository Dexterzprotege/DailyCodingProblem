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



