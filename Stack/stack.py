class Stack:
    def __init__(self, maxnelemns) -> None:
        self.dados = [0] * maxnelemns
        self.elements = 0

    def insert(self, x):
        if self.elements == len(self.dados):
            return False
        for i in range(self.elements):
            if self.dados[i] == x:
                return False
        self.dados[self.elements] = x    
        self.elements += 1    
        return True

    def remove(self):
        if self.elements == 0:
            return False
        self.elements -= 1
        return True

    def top(self):
        if self.elements == 0:
            return (False,-1)
        return (True, self.dados[self.elements - 1])

stack = Stack(10)
stack.insert(1)
stack.insert(2)
stack.insert(110)
print(stack.top())
stack.remove()
print(stack.top())

print(stack.dados)