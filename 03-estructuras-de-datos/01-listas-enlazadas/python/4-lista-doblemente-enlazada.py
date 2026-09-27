class Node:
    def __init__(self,data):
        self.data = data
        self.next = None #enlace que apunta al siguiente nodo en la cadena
        self.prev = None #enlace que apunta al anterior nodo en la cadena

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2

node2.prev = node1 #ej: el nodo 2 apunta al nodo siguiente 1
node2.next = node3 #ej: el nodo 2 apunta al nodo anterior 3

node3.prev = node2
node3.next = node4

node4.prev = node3

print("Traversing forward: ") #avanzando hacia adelante
currentNode = node1
while currentNode:
    print(currentNode.data, end= " -> ")
    currentNode = currentNode.next
print("Null")

print("Traversing backward") #avanzando hacia atras
currentNode = node4
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev
print("Null")