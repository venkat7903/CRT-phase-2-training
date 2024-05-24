class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None 

def insertIntoBST(root, val):
    if root == None:
        return Node(val)
    elif root.val > val:
        root.left = insertIntoBST(root.left, val)

    elif root.val < val:
        root.right = insertIntoBST(root.right, val)

    return root

def PrintTree(root):
    if root == None:
        return 
    result = []
    Q = [root]

    while len(Q) > 0:
        sublist = []
        n = len(Q)

        for i in range(n):
            curr = Q.pop(0)
            sublist.append(curr.data)

            if curr.left != None:
                Q.append(curr.left)

            if curr.right != None:
                Q.append(curr.right)

        result.append(sublist)
    print(result)