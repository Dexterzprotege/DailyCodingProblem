# This problem was asked by Google.
# Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
# For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
# In this example, assume nodes with the same value are the exact same node objects.
# Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def countt(root):
    c=0
    while root!=None:
        c+=1
        root=root.next
    return c
def intersection(a,b):
    c1=countt(a)
    c2=countt(b)
    if c1>c2:
        return getInt(c1-c2,a,b)
    else:
        return getInt(c2-c1,b,a)
def getInt(d,node1,node2):
    cur1=node1
    cur2=node2
    for i in range(d):
        if cur1==None:
            return -1
        cur1=cur1.next
    while cur1!=None and cur2!=None:
        if cur1.data==cur2.data:
            return cur1.data
        cur1=cur1.next
        cur2=cur2.next
    return -1
root=Node(3)
root.next=Node(7)
root.next.next=Node(8)
root.next.next.next=Node(14)
root.next.next.next.next=Node(10)
root.next.next.next.next.next=Node(6)

root2=Node(99)
root2.next=Node(1)
root2.next.next=Node(5)
root2.next.next.next=root.next.next.next.next
print("Node intersection is:",intersection(root,root2))