class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DLinkedList():
    def __init__(self):
        self.first = None

    def find(self, x):
        p = self.first
        while(p != None):
            if p.value == x:
                return (True, p)
            p = p.next
        return (False, None)

    def insert(self, x):
        node = Node(x)
        isValid, el = self.find(x)
        if isValid:
            return False
        if self.first == None:
            self.first = node
            return True
        self.first.prev = node
        node.next = self.first
        self.first = node
        return True

    def remove(self, x):
        if self.first == None:
            return False
        isValid, el = self.find(x)
        if not isValid:
            return False
        if el.prev:
            el.prev.next = el.next
        else:
            self.first = el.next
        if el.next:
            el.next.prev = el.prev
        return True
            
        

dll = DLinkedList()
dll.insert(10)
dll.insert(20)
print(dll.find(10))
print(dll.insert(10))
print(dll.remove(10))
print(dll.remove(30))
print(dll.remove(20))
print(dll.remove(50))
print(dll.find(10))