from Node import Node
from LinkedList import LinkedList

# Declaramos nuestra funcion Main
def __main__():
    
    # Definimos una instancia de LinkedList
    myList = LinkedList()
    
    myList.append("A")
    myList.append("B")
    myList.append("C")
    myList.append("D")
    myList.append("E")
    myList.append("F")
    myList.append(1)
    myList.append(3.6)
    
    print(myList)
    print(f"Elementos en la lista: {myList.__len__()}")
    
    myList.remove("C")
    myList.remove(0)
    
    print(myList)
    print(f"Elementos en la lista: {myList.__len__()}")
    
# Mandamos a llamar la funcion main   
__main__()