# Go to root file and run:
# python linked_list.py

# Test Cases:

# 1. Empty linked list 
# 2. Not empty linked list
#  2.1 Already have the value
#  2.2 Doesn't have the value

class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.first = None
    
    def append(self, node: Node) -> bool:
        initNode = self.first
        if initNode == None:
            self.first = node
            return True
        while initNode.next != None:
            if initNode.value == node.value:
                return False
            initNode = initNode.next
        initNode.next = node
        return True

    def search(self, value: int) -> bool:
        node = self.first
        while node != None:
            if node.value == value:
                return True
            node = node.next
        return False

    def show(self) -> None:
        node = self.first
        while node != None:
            print(node.value)
            node = node.next

    def remove(self, value: int) -> bool:
        node = self.first
        if node == None:
            return False
        if node.value == value:
            self.first = node.next
            return True
        while node.next != None:
            if node.next.value == value:
                node.next = node.next.next
                return True
            node = node.next
        if node != None:
            if node.value == value:
                return True
        return False
                    

linkedList = LinkedList()
linkedList.append(Node(10))
linkedList.append(Node(20))
linkedList.append(Node(10))
print(linkedList.remove(40))
print(linkedList.search(50))
print(linkedList.search(20))

linkedList.append(Node(30))
linkedList.append(Node(40))
linkedList.append(Node(32))
linkedList.show()
