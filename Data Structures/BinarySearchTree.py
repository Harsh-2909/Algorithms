class Node():

    def __init__(self, data: int):
        self.data = data
        self.left = self.right = None
    
    def __str__(self):
        return f"{self.data}"

class BinarySearchTree(Node):

    def __init__(self, data = None):
        if data is None:
            self.root = None
        else:
            self.root = Node(data)

    def insert(self, data: int) -> None:
        current = self.root
        while current != None:
            if current.data >= data:
                current = current.left
            else:
                current = current.right
        current = Node(data)
    
    def find(self, data: int) -> bool:
        current = self.root
        while current != None:
            if current.data == data:
                return True
            elif current.data > data:
                current = current.left
            else:
                current = current.right
        return False
    
    # def remove(self, data: int) -> str:
    #     if not self.find(data):
    #         return f"{data} is not present in BST."
    
if __name__ == '__main__':
    tree = BinarySearchTree(23)
    tree.insert(20)
    tree.insert(30)
    tree.insert(10)
    tree.insert(15)
            
