class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None 

def printQueue(head):
    while head:
        print(head.data, end="->")
        head = head.next
    print(None)

def enQueue(head, ele):
    temp = Node(ele)
    if head == None:
        return temp 
    tail = head 
    while tail.next != None:
        tail = tail.next
    tail.next = temp 
    return head 

def deQueue(head):
    if head == None or head.next == None:
        return None 
    temp = head.next
    head.next = None 
    return temp 

num = list(range(10, 110, 10))
head = None
for i in num:
    head = enQueue(head, i)
printQueue(head)
head = deQueue(head)
printQueue(head)