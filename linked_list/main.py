class Node:
    def __init__(self, value, next = None) -> None:
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    # O(1)
    def unshift(self, value):
        self.head = Node(value, self.head)

    # O(1)
    def shift(self):
        self.head = self.head.next

    # O(n)
    def push(self, value):
        newNode = Node(value)

        if self.head == None:
            self.head = newNode
            return

        current = self.head
        while current.next != None:
            current = current.next
        
        current.next = newNode

    # O(n)
    def pop(self):
        if self.head == None:
            return

        current = self.head

        while current.next != None and current.next.next != None:
            current = current.next
        
        current.next = None

    def __str__(self):
        output = ""
        current = self.head
        
        while current != None:
            output += str(current.value) + ", "
            current = current.next
        
        return output


linked_list = LinkedList()

linked_list.push(1)
print(linked_list)

linked_list.push(2)
print(linked_list)

linked_list.unshift(0)
print(linked_list)

linked_list.shift()
print(linked_list)

linked_list.pop()
print(linked_list)
 