class Lista:
    def __init__(self, maxnelemns: int) -> None:
        self.dados: list[int] = [0] * maxnelemns
        self.nelemens = 0
        self.maxnelemns = maxnelemns

    def find(self, x):
        for i in range(self.nelemens):
            if self.dados[i] == x:
                return True
        return False

    def insert(self, value: int) -> bool:
        if self.find(value):
            return False
        if self.nelemens == self.maxnelemns:
            return False
        self.dados[self.nelemens] = value
        self.nelemens += 1
        return True

    def remove(self, x:int) -> bool:
        if self.nelemens == 0:
            return False
        i = 0
        while(i < self.nelemens) and (self.dados[i] != x):
            i += 1
        if (i == self.nelemens):
            return False
        self.dados[i] = self.dados[self.nelemens - 1]
        self.nelemens -= 1
        return True
    
    def smaller(self) -> (bool, int):
        if self.nelemens == 0:
            return (False, -1)
        smaller = self.dados[0]
        for i in range(self.nelemens):
            if self.dados[i] < smaller:
                smaller = self.dados[i]
        return (True, smaller)

    def odd_quantity(self) -> (bool, int):
        if self.nelemens == 0:
            return (False, -1)
        quantity = 0
        for i in range(self.nelemens):
            if(self.dados[i] % 2):
                quantity += 1
        return (True, quantity)

    def average(self) -> (bool, float):
        if self.nelemens == 0:
            return (False, 0.0)
        average = 0
        for i in range(self.nelemens):
            average += self.dados[i]
        average = average / self.nelemens
        return (True, average)
        
    def sum_all_elements(self) -> int:
        if self.nelemens == 0:
            return 0
        sumA = 0
        for i in range(self.nelemens):
            sumA += self.dados[i]
        return sumA

    def sum_of_squares(self) -> int:
        if self.nelemens == 0:
            return 0
        sumS = 0
        for i in range(self.nelemens):
            sumS += self.dados[i] ** 2
        return sumS

    def removeOrdinal(self, k: int) -> (bool, int):
        if k <= 0 or k > self.nelemens:
            return (False, -1)
        removed = self.dados[k - 1]
        self.nelemens -= 1
        self.dados[k - 1] = self.dados[self.nelemens]
        return (True, removed)

arr = Lista(5)

print(arr.insert(3))
print(arr.insert(4))
print(arr.insert(2))
print(arr.insert(4))
print(arr.dados)
print(arr.removeOrdinal(1))
print(arr.dados)
