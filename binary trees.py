class Box:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None 

def printPreOrderTraversal(root):
    if root == None:
        return 
    print(root.data, end=" ")
    printPreOrderTraversal(root.left)
    printPreOrderTraversal(root.right)

def printInorderTraversal(root):
    if root == None:
        return 
    printInorderTraversal(root.left)
    print(root.data, end=" ")
    printInorderTraversal(root.right)

def printPostOrderTraversal(root):
    if root == None:
        return 
    printPostOrderTraversal(root.left)
    printPostOrderTraversal(root.right)
    print(root.data, end=" ")

def levelOrderTraversal(root):
    if root == None:
        return 
    result = []
    Q = [root]

    while len(Q) > 0:
        n = len(Q)
        subresult = []
        for i in range(n):
            currNode = Q.pop(0)
            subresult.append(currNode.data)

            if currNode.left != None:
                Q.append(currNode.left)
            
            if currNode.right != None:
                Q.append(currNode.right)

        result.append(subresult)
    print(result)

def findLeftView(root):
    if root == None:
        return []
    result = []
    Q = [root]
    while len(Q) > 0:
        n = len(Q)
        for i in range(n):
            curr = Q.pop(0)
            if i == 0:
                result.append(curr.data)
            if curr.left != None:
                Q.append(curr.left)
            if curr.right != None:
                Q.append(curr.right)
    print(result)

# def topViewHelper(root, store, hd, level):
#     if root == None:
#         return 
 
#     if hd not in store or store[hd][0] > level:
#         store[hd] = [level, root.data]
 
#     topViewHelper(root.left, store, hd - 1, level + 1)
#     topViewHelper(root.right, store, hd + 1, level + 1)
 
# def findTopView(root):
#     result = []
#     if root == None:
#         return result
 
#     store = {}
#     topViewHelper(root, store, 0, 0)
#     sortedKeys = sorted(store.keys())
#     print(sortedKeys)
#     for key in sortedKeys:
#         result.append(store[key][1])
#     print(result)

def topViewHelper(root, store, hd, level):
    if root == None:
        return 
    if hd not in store or store[hd][0] > level:
        store[hd] = [level, root.data]

    topViewHelper(root.left, store, hd-1, level+1)
    topViewHelper(root.right, store, hd+1, level+1)

def findTopView(root):
    result = []
    if root == None:
        return 
    
    store = {}
    topViewHelper(root, store, 0, 0)

    sortedKeys = sorted(store.keys())
    for key in sortedKeys:
        result.append(store[key][1])
    print(result)

root = Box(1)
n1 = Box(2)
n2 = Box(3)
n3 = Box(4)
n4 = Box(5)
n5 = Box(6)
n6 = Box(7)
n7 = Box(8)
n8 = Box(9)
n9 = Box(10)
n10 = Box(11)
n11 = Box(12)
n12 = Box(13)
n13 = Box(14)
n14 = Box(15)

root.left = n1 
root.right = n2 
n1.left = n3 
n1.right = n4 
n2.left = n5 
n2.right = n6 
n3.left = n7 
n3.right = n8 
n4.left = n9 
n4.right = n10 
n5.left = n11
n5.right = n12 
n6.left = n13 
n6.right = n14

printPreOrderTraversal(root)
print()
printInorderTraversal(root)
print()
printPostOrderTraversal(root)
print()
levelOrderTraversal(root)
findLeftView(root)
findTopView(root)