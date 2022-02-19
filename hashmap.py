"""
Principe : convertit une clé en index qui sert à localiser la valeur associé à l'aide d'une fonction de hashage
But : Permet de simplifier les taches de recherches

V1 : 
Création d'une fonction de hashage simple mais non persistante : ASCII numbers, chaque lettre nous fournit son index ascii.
On somme les indexs des ascii de notre clé modulo la taille de la mémoire préalloué.

V2: 
Utilisation des chaines pour éviter les collisions. Des qu'une collision est rencontré on ajoute à la liste le couple (key,value).

V3: A faire
Linear probing. Des qu'on observe une collision on regarde si l'adresse suivante est libre pour le stockage. 
Si elle ne l'est pas on commence au debut et on stocke des qu'on trouve un emplacement libre.
"""
def hash_ascii(key,memory_size):
    s = 0 
    for char in key:
        s += ord(char)
    return s % memory_size

class SimpleHashMap: 
    def __init__(self,memory_size = 10):
        self.memory_size = memory_size #mémoire de la table de hashage à préalloué 
        self.list = [None for _ in range(self.memory_size)]
        self.hash_ascii = hash_ascii
    
    def __getitem__(self,key): #Operateur []
        index = self.hash_ascii(key,self.memory_size)
        return self.list[index]
    
    def __setitem__(self,key,val): #Operateur []
        index = self.hash_ascii(key,self.memory_size)
        self.list[index] = val 
    
    def __delitem__(self,key): #Operateur del
        index = self.hash_ascii(key,self.memory_size)
        self.list[index] = None
        
        
class ChainedHashMap:
    def __init__(self,memory_size = 10):
        self.memory_size = memory_size #mémoire de la table de hashage à préalloué 
        self.list = [[] for _ in range(self.memory_size)]
        self.hash_ascii = hash_ascii
        
    def __getitem__(self,key): #Operateur []
        index = self.hash_ascii(key,self.memory_size)
        for el in self.list[index]:
            if(el[0] == key):
                return el[1]
    
    def __setitem__(self,key,val): #Operateur []
        index = self.hash_ascii(key,self.memory_size)
        found = False
        for i,el in enumerate(self.list[index]):
            if(el[0] == index and len(el)==2):
                self.list[index][i] = val
                found = True 
        if(not found):
            self.list[index].append((key,val))
            
    def __delitem__(self,key):
        index = self.hash_ascii(key,self.memory_size)
        for i,el in enumerate(self.list[index]):
            if(el[0] == index ):
                del self.list[index][i]
                
    
if __name__ == '__main__':
    n = 10 
    simple_dict = SimpleHashMap(n)
    chained_dict = ChainedHashMap(n)
    
    key1 = 'Nom' ; val1 = 'Durand'
    key2 = 'Lost'; val2 = True
    
    #Problème SimpleHashMap quand 2 key ont les memes indices avec notre fonction de hash 
    simple_dict[key1] = val1 
    simple_dict[key2] = val2
    
    print(simple_dict[key1]) #On obtient True au lieu de 'Durand' ce qui est un problème 
    
    #Résolution à l'aide de chaines 
    chained_dict[key1] = val1 
    chained_dict[key2] = val2
    
    print(chained_dict[key1]) #On récupere bien 'Durand' comme on le souhaitait 
    
    
    
    
    
    
    
    
    
    
