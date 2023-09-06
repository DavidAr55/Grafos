from Node import Node

class LinkedList:
    
    # Constructor de LinkedList
    def __init__(self):
        self.frist = None
        self.size = 0
    
    # Funcion para agregar un Nodo
    def append(self, value):
        myNode = Node(value)
        
        # Si la lista está vacia, generamos el primero nodo con myNode
        if self.size == 0:
            self.frist = myNode
        
        # Agregamos el nodo en el ultimo lugar de la lista
        else:
            current = self.frist
            while current.next != None:
                current = current.next
                
            current.next = myNode
            
        self.size += 1
        return myNode
    
    # Generamos la funcion para eliminar elgun nodo de la lista
    def remove(self, value):
        # Si la lista está vacía, no hay nada que eliminar
        if self.size == 0:
            return False
        
        # Si el valor que queremos eliminar es el primer nodo de la lista
        if self.frist.value == value:
            deletedNode = self.frist
            self.frist = self.frist.next
            self.size -= 1
            return deletedNode

        # Si el valor que queremos eliminar está en el medio o al final de la lista
        current = self.frist
        while current.next is not None:
            if current.next.value == value:
                deletedNode = current.next
                current.next = current.next.next
                self.size -= 1
                return deletedNode
            current = current.next

        # Si el valor no se encuentra en la lista
        return False
    
    # Funcion paara ver el tamaño de la lista
    def __len__(self):
        return self.size
    
    # Funcion para imprimir la lista
    def __str__(self):
        string = "["
        current = self.frist
        
        while current != None:
            string += str(current) + ", "
            current = current.next
            
        string += "]"
        return string