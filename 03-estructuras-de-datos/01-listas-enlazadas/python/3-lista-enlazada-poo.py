class Nodo:
    """Clase que representa un elemento individual de la lista."""
    def __init__(self, dato):
        self.dato = dato      # El valor que guardamos
        self.siguiente = None # Puntero al siguiente nodo (inicialmente None)

class ListaEnlazada:
    """Clase que maneja la estructura de la lista."""
    def __init__(self):
        self.cabeza = None # El inicio de la lista (Head)

    def esta_vacia(self):
        """Verifica si la lista no tiene elementos."""
        return self.cabeza is None

    def agregar_al_final(self, dato):
        """Inserta un nuevo nodo al final de la lista."""
        nuevo_nodo = Nodo(dato)

        # Caso 1: Si la lista está vacía, el nuevo nodo es la cabeza
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return

        # Caso 2: Recorrer la lista hasta encontrar el último nodo
        ultimo = self.cabeza
        while ultimo.siguiente: # Mientras exista un "siguiente"
            ultimo = ultimo.siguiente
        
        # Enlazar el último nodo encontrado con el nuevo
        ultimo.siguiente = nuevo_nodo

    def agregar_al_inicio(self, dato):
        """Inserta un nuevo nodo al principio de la lista."""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza # El nuevo apunta a la antigua cabeza
        self.cabeza = nuevo_nodo           # Actualizamos la cabeza

    def imprimir_lista(self):
        """Imprime los elementos de la lista visualmente."""
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(str(actual.dato))
            actual = actual.siguiente
        print(" -> ".join(elementos) + " -> None")

    def eliminar_nodo(self,key):
        """Elimina la primera aparición de 'key' en la lista."""
        # Verificar si la lista está vacía
        if self.cabeza is None:
            return 
        
        # Caso 1: El nodo a borrar es la cabeza (Head)
        if self.cabeza.dato == key:
            self.cabeza = self.cabeza.siguiente
            return
        
        # Se recorre el nodo Anterior al que se quiere borrar
        actual = self.cabeza

        # Mientras haya un siguiente nodo Y ese siguiente no sea el que buscamos
        while actual.siguiente and actual.siguiente.dato != key:
            actual = actual.siguiente
        
        # Se verifica por qué se detuvo el bucle
        if actual.siguiente is None:
            print(f"El valor {key} no se encontró en la lista.")
            return # Llegamos al final y no estaba
        
        # 5. ELIMINACIÓN: Saltamos el nodo (el enlace pasa por encima)
        # 'actual' es el nodo previo. 'actual.siguiente' es el que borramos.
        actual.siguiente = actual.siguiente.siguiente
        


# --- Prueba del código ---

# 1. Crear la lista
lista = ListaEnlazada()

# 2. Agregar elementos
lista.agregar_al_final(10)
lista.agregar_al_final(20)
lista.agregar_al_final(30)

# 3. Agregar al inicio
lista.agregar_al_inicio(5)

# 4. Mostrar resultado
print("Estado final de la lista:")
lista.imprimir_lista()

print("Borrando 20...")
lista.eliminar_nodo(20)
lista.imprimir_lista() # 10 -> 30 -> None