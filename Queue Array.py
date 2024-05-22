def enqueue(Q, ele):
    Q.append(ele)
    print(ele, "Enqueued Success")

def deque(Q):
    if len(Q) == 0:
        print("Queue is Empty")
        return 
    print(Q[0], "Ele is deleted")
    Q.pop(0)

Q = []
deque(Q)
enqueue(Q, 10)
enqueue(Q, 20)
enqueue(Q, 30)

deque(Q)
deque(Q)
deque(Q)
deque(Q)
print(Q)