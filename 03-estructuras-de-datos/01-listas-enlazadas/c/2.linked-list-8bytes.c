#include <stdio.h>
#include <stdlib.h>

//Se declara una estructura llamada Node
typedef struct Node 
{
    int data;               //Dato que almacena el nodo
    struct Node* next;      //Puntero al siguiente nodo de la lsita

} Node;


Node* createNode(int data)
{
    Node* newNode = (Node*)malloc(sizeof(Node));    // Reserva memoria dinámica suficiente para un Node.

    if (!newNode)
    {                                  // Verifica si la reserva de memoria falló (si malloc devolvió NULL).
            printf("Memory allocation failed!");
            exit(1);
    }

    newNode -> data = data;     //Asigna el valor del nodo. Guarda el valor que recibes como argumento.
    newNode -> next =  NULL;    // El siguiente nodo todavia no existe. Inicializa el puntero al siguiente nodo en NULL, porque este nodo aún no apunta a otro.
    
    return newNode;             //Devuelve la dirección del nuevo nodo creado en memoria.
}

//función para recorrer e imprimir los valores de una lista enlazada.

void printList(Node* node)      //imprime todos los valores a partir de este nodo hacia adelante. 
//Node* node → recibe como parámetro un puntero al primer nodo de la lista
{   
    while (node)                 // cualquier puntero distinto de NULL se considera verdadero
    //este bucle se ejecuta mientras node no se NULL
    {
        printf("%d ->", node -> data);  //imprime el valor almacenado en el nodo actual.
        node = node -> next;            //mueve el puntero al siguiente nodo en la lista.

    }
    //Cuando node apunta a NULL, significa que ya no hay más nodos que imprimir y el bucle termina.
}
//De esta manera, la función “camina” nodo por nodo a través de la lista enlazada.

int main() 
{
    /*
    Llama a la función createNode(int data), que hace lo siguiente:
        - Reserva memoria dinámica con malloc.
        - Asigna el valor (data).
        - Inicializa el puntero next en NULL.
        - Devuelve la dirección de memoria del nuevo nodo.
    */
    Node* node1 = createNode(3);
    Node* node2 = createNode(5);
    Node* node3 = createNode(13);
    Node* node4 = createNode(2);

    //Enlazar los nodos
    node1 -> next = node2;
    node2 -> next = node3;
    node3 -> next = node4;

    printList(node1);

    //Liberar la memoria
    free(node1);
    free(node2);
    free(node3);
    free(node4);

    return 0;
}

/*

createNode(3)
createNode(5)
createNode(13)
createNode(2)
      ↓
 [3] → [5] → [13] → [2] → NULL
      ↓
 printList(node1)
      ↓
 free(node1..4)

*/
