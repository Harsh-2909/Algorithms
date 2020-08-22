class Node():

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

class SinglyLinkedList(Node):
    seperator = ' '

    def __init__(self, data = None):
        if data is None:
            self.head = None
        else:
            self.head = Node(data)
    
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
            raise IndexError("SinglyLinkedList index out of range")
        current = self.head
        while key:
            current = current.next
            key -= 1
        return current.data

    def insertAtBeginning(self, data) -> None:
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode
    
    def insertAtEnd(self, data) -> None:
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
    
    def deleteFromBeginning(self) -> str:
        if self.head == None:
            return "LinkedList is empty"
        
        current = self.head
        self.head = self.head.next
        deleted_data = current.data
        del current
        return deleted_data
    
    def deleteFromEnd(self) -> str:
        if self.head == None:
            return "LinkedList is empty"
        
        current = self.head
        if current.next == None:
            to_delete = current
            self.head = None
        else:
            while current.next.next is not None:
                current = current.next
            to_delete = current.next
            current.next = None
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
    a = SinglyLinkedList(5)
    print(len(a))
    print(a.isEmpty)