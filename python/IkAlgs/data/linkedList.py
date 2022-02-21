class LinkedList:
    def __init__(self):
        self.head = None

    class Node:
        def __init__(self, x):
            self.x = x
            self.next = None

    def push(self, x):
        nN = self.Node(x)
        if self.head != None:
            nN.next = self.head
        self.head = nN

    def pop(self):
        if self.head != None:
            val = self.head.x
            self.head = self.head.next
            return val


ll = LinkedList()
ll.push(1)
ll.push(2)
print(ll.pop())
print(ll.pop())
print(ll.pop())
print(ll.pop())
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1)
print(ll.pop())
print(ll.pop())
print(ll.pop())
print(ll.pop())
