class Queue:
    def __init__(self, maxnelemns:int) -> None:
        self.dados: list[int] = [0] * maxnelemns
        self.prim = 0
        self.nelemens = 0 

    def insert(self, x: int) -> bool:
        if self.nelemens == len(self.dados):
            return False
        for i in range(self.nelemens):
            if self.dados[(self.prim + i) % len(self.dados)] == x:
                return False
        self.dados[(self.prim + self.nelemens) % len(self.dados)] = x
        self.nelemens += 1
        return True
    
    def remove(self) -> bool:
        if self.nelemens == 0:
            return False
        self.prim = (self.prim + 1) % len(self.dados)
        self.nelemens -= 1
        return True

    def front(self) -> (bool, int):
        if self.nelemens == 0:
            return (False, -1)
        return (True, self.dados[self.prim])

queue = Queue(9)
print(queue.insert(10))
print(queue.insert(2))
print(queue.insert(3))
print(queue.front())
queue.remove()
print(queue.front())
queue.remove()
print(queue.front())
queue.remove()