class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)

class DoublyLinkedList(Node):
    seperator = ' '

    def __init__(self, data = None):
        if data is None:
            self.head = self.tail = None
        else:
            self.head = self.tail = Node(data)
            
    
    def __str__(self):
        nodes = []
        current = self.head
        while current:
            nodes.append(current)
            current = current.next
        return self.seperator.join(str(node) for node in nodes)
    
    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    
    def __getitem__(self,key):
        if key < 0 or key >= len(self):
            raise IndexError("DoublyLinkedList index out of range")
        current = self.head
        while key:
            current = current.next
            key -= 1
        return current.data

    def insertAtBeginning(self, data) -> None:
        newnode = Node(data)
        if self.head == None:
            self.head = self.tail = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
    
    def insertAtEnd(self, data) -> None:
        newnode = Node(data)
        if self.head == None:
            self.head = self.tail = newnode
        else:
            current = self.tail
            current.next = newnode
            newnode.prev = current
            self.tail = newnode
    
    def deleteFromBeginning(self) -> str:
        if self.head == None:
            return "List is empty"
        
        current = self.head
        to_delete = current
        if current.next == None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        deleted_data = to_delete.data
        del to_delete
        return deleted_data
    
    def deleteFromEnd(self) -> str:
        if self.head == None:
            return "List is empty"
        
        current = self.head
        if current.next == None:
            to_delete = current
            self.head = self.tail = None
        else:
            to_delete = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
        deleted_data = to_delete.data
        del to_delete
        return deleted_data
    
    def toList(self) -> list:
        current = self.head
        while current:
            yield current.data
            current = current.next
    
    def setSeperator(self, seperator: str = ' ') -> None:
        self.seperator = seperator
    
    def getSeperator(self) -> str:
        return self.seperator
    
    @property
    def isEmpty(self):
        return self.head is None

if __name__ == "__main__":
    a = DoublyLinkedList()
    print(a.isEmpty)
    a.insertAtBeginning(5)
    a.insertAtEnd(6)
    
    print(a[0], a[len(a)-1])
