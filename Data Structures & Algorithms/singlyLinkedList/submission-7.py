from typing import List

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        
        curr = self.head
        for _ in range(index):
            curr = curr[1]
        
        return curr[0]

    def insertHead(self, val: int) -> None:
        node = [val, self.head]
        self.head = node
        if self.size == 0:
            self.tail = node
        self.size += 1

    def insertTail(self, val: int) -> None:
        node = [val, None]
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail[1] = node
            self.tail = node
        self.size += 1

    def remove(self, index: int) -> bool:
        if index >= self.size:
            return False
        
        if index == 0:
            self.head = self.head[1]
            if self.size == 1:
                self.tail = None
            self.size -= 1
            return True
        
        curr = self.head
        for _ in range(index - 1):
            curr = curr[1]
        
        if curr[1] == self.tail:
            self.tail = curr
        
        curr[1] = curr[1][1]
        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr[0])
            curr = curr[1]
        return res
