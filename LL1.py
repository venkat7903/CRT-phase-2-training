class Node():
    def __init__(self, data):
        self.data = data
        self.next = None 

def printLL(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print(None)

obj1 = Node(10)
obj2 = Node(20)
obj3 = Node(30)

obj1.next = obj2
obj2.next = obj3 

# printLL(obj1)

def insertAtEnd(head, ele):
    temp = Node(ele)
    if head == None:
        return temp 
    tail=head
    while tail.next != None:
        tail = tail.next
    tail.next = temp 
    return head 

def insertAtBegining(head, ele):
    temp = Node(ele)
    if head == None:
        return temp 
    temp.next = head 
    return temp


def insertAtParticularNode(head, pos, ele):
    temp = Node(ele)
    c = 0
    tail = head
    while c != pos:
        c += 1
        tail = tail.next
    tempo = tail.next
    tail.next = temp 
    temp.next = tempo
    return head 
         
    

def deleteAtLast(head):
    curr = head 
    if curr == None or curr.next == None:
        return None 
    while curr.next.next != None:
        curr = curr.next 
    curr.next = None
    return head

def deleteAtBegin(head):
    if head == None or head.next == None:
        return None
    temp = head.next
    head.next = None
    return temp 

def deleteAtSpecificPos(head, pos):
    if pos == 0:
        return deleteAtBegin(head)
    c = 0
    tail = head
    while c != pos - 1:
        c+=1
        tail = tail.next
    nodeToBeDeleted = tail.next
    tail.next = nodeToBeDeleted.next 
    nodeToBeDeleted.next = None 
    return head


num = list(range(10, 110, 10))
head = None
for i in num:
    head = insertAtEnd(head, i)

printLL(head)

head = insertAtBegining(head, 110)
printLL(head)
head = deleteAtLast(head)
printLL(head)
head = deleteAtBegin(head)
printLL(head)
head = insertAtParticularNode(head, 3, 200)
printLL(head)
head = deleteAtSpecificPos(head, 3)
printLL(head)
head = deleteAtSpecificPos(head, 8)
printLL(head)