class Node:
    def __init__(self,data):
        self.data=data
        self.next=None #es un puntero o enlace que apunta al siguiente nodo en la cadena

node1 = Node(3) 
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2 #ej: el nodo 1 (dato 3) apunta al nodo 2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end = " -> ")
    currentNode = currentNode.next 

print("Null")