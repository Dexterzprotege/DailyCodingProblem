class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def unival(root):
    if root==None:
        return True
    if root.left!=None and root.left.data!=root.data:
        return False
    if root.right!=None and root.right.data!=root.data:
        return False
    if unival(root.left) and unival(root.right):
        return True
    return False
def count(root):
    if root==None:
        return 0
    c=count(root.left)+count(root.right)
    if unival(root):
        c+=1
    return c
def count2(root):
    if root is None:
        return 0, True
    left_count, is_left_unival = count2(root.left)
    right_count, is_right_unival = count2(root.right)
    total_count = left_count + right_count
    if is_left_unival and is_right_unival:
        if root.left is not None and root.data != root.left.data:
            return total_count, False
        if root.right is not None and root.data != root.right.data:
            return total_count, False
        return total_count + 1, True
    return total_count, False
root=Node(0)
root.left=Node(1)
root.right=Node(0)
root.right.left=Node(1)
root.right.right=Node(0)
root.right.left.right=Node(1)
root.right.left.left=Node(1)
print("No.of unival trees:",count(root))
print("No.of unival trees(Method 2):",count2(root)[0])