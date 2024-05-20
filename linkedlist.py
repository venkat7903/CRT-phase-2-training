class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None

def printLinkedList(curr):
    while curr != None:
        print(curr.data, end="->")
        curr = curr.next
    print(None)
def count(curr):
    c=0
    while curr != None:
        print(curr.data, end="->")
        curr = curr.next
    print(None)
# Block creation is happening
obj1 = Box(10)
obj2 = Box(20)
obj3 = Box(30)
obj4 = Box(40)

# establishing links in below 4 lines
obj1.next = obj2
obj2.next = obj3 
obj3.next = obj4
obj4.next = None

printLinkedList(obj1)

def insertAtTailNode(head, ele):
    temp = Box(ele)
    if head == None:
        return temp 
    tail = head 

    while tail.next != None:
        tail = tail.next 
    tail.next = temp 
    return head 

def insertionAtBegining(head, ele):
    temp = Box(ele)
    if head == None:
        return temp 
    temp.next = head 
    return temp 

def insertionAtParticularNode(head, pos, ele):
    c = 0
    temp = Box(ele)
    tail = head
    while tail.next:
        c += 1
        if c == pos:
            temp.next = tail.next
            tail.next = temp 
            return head
        tail = tail.next
    return head

head = None

nums = [i for i in range(10, 110, 10)]
for i in nums:
    head = insertAtTailNode(head, i)

head=insertionAtBegining(head,69)

# printLinkedList(head)
# # head = Box(10)
# head=insertAtTailNode(head, 100)
# printLinkedList(head)
head = insertionAtParticularNode(head, 2, 1000)
printLinkedList(head)