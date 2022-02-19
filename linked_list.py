"""
Principe : lien entre la reference de l'element actuel et celui qui le suit, on parle de "contiguous memory location"
But : Permet de simplifier les taches d'insertion et de suppression comparé à l'utilisation de simples listes, pas besoin de préallocation
"""

class Node:
    def __init__(self,data=None,next=None):
        
        self.data = data #donnée du noeud
        self.next = next #pointeur pour l'element suivant

class LinkedList:
    def __init__(self):
        self.head = None #pointeur qui pointe sur le début de notre liste
    
    def __len__(self):
        c = 0 
        itr = self.head
        while(itr):
            c+=1
            itr = itr.next
        return c 
    
    def start_insert(self,data):
        self.head = Node(data, self.head) 
        
    def append(self,data):
        if self.head is None:  
            self.head = Node(data,None)
            return 
        
        itr = self.head 
        while(itr.next): #On parcourt notre linked list jusqu'a atteindre None qui est la fin 
            itr = itr.next 
            
        itr.next = Node(data,None)
        
    def append_list(self,data_list):
        self.head = None #On passe directement à la fin de notre liste 
        for value in data_list:
            self.append(value)
            
        
    def insert(self,data,index):
        
        if(index < 0 or index > self.__len__()):
            raise Exception("Index Invalide")    
        elif(index == 0):
            self.start_insert(data)
        elif(index == self.__len__()):
            self.append(data)
            
        c = 0 
        itr = self.head
        while(itr):
            if(c == index-1): #On s'arrete un noeud avant l'index qu'on veut ajouter 
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            c += 1
    
    def remove(self,index):
        if(index < 0 or index > self.__len__()):
            raise Exception("Out of range")    
        
        if(index == 0):
            self.head = self.head.next
            return 
        
        c = 0
        itr = self.head
        while(itr):
            if(c == index - 1):
                itr.next = itr.next.next #On saute le noeud l'index voulu
                break
            itr = itr.next
            c += 1 
            
    def summary(self):
        if(self.head is None):
            print("--Linked List Empty--")
            return 
        r = ''
        itr = self.head
        while(itr):
            r += str(itr.data) + ' -> ' if itr.next is not None else str(itr.data)
            itr = itr.next
        print(r)
            
if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.append_list([0,1,2,3,4,5,6,7,8,9,10])
    
    linked_list.summary()
    
    linked_list.remove(5)
    linked_list.summary()
    
    
    