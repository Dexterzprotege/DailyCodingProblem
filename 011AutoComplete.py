# This problem was asked by Twitter.
# Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.
# For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].
# Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.

class Node:
    def  __init__(self,character):
        self.character=character
        self.children=[None]*26
        self.leaf=False
        self.visited=False
    def setChild(self,node,index):
        self.children[index]=node
    def getChild(self,val):
        return self.children[val]
    def getChildren(self):
        return self.children
    def getCharacter(self):
        return self.character
    def setCharacter(self,character):
        self.character=character
    def setLeaf(self,val):
        self.leaf=val
    def getLeaf(self):
        return self.leaf
    def setVisited(self,val):
        self.visited=val
    def getVisited(self):
        return self.visited

class Trie:
    def __init__(self):
        self.root=Node("")
    def insert(self,key):
        temp=self.root
        for i in key:
            ascii=ord(i)-ord('a')
            if temp.getChild(ascii)==None:
                node=Node(i)
                temp.setChild(node,ascii)
                temp=node
            else:
                temp=temp.getChild(ascii)
        temp.setLeaf(True)
    def search(self,key):
        temp=self.root
        for i in key:
            ascii=ord(i)-ord('a')
            if temp.getChild(ascii)==None:
                return False
            else:
                temp=temp.getChild(ascii)
        return True
    def autoComplete(self,prefix):
        temp=self.root
        res=[]
        for i in prefix:
            ascii=ord(i)-ord('a')
            temp=temp.getChild(ascii)
        self.collect(temp,prefix, res)
        return res
    def collect(self,node,prefix,res):
        if node==None:
            return
        if node.getLeaf():
            res.append(prefix)
        for childNode in node.getChildren():
            if childNode==None:
                continue
            childCharacter= childNode.getCharacter()
            self.collect(childNode,prefix+childCharacter,res)

words=[str(x) for x in input("Enter dictionary: ").split()]
query=str(input("Enter Query String: "))
trie=Trie()
for i in words:
    trie.insert(i)
print(trie.autoComplete(query))