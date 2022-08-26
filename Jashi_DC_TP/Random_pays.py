# module utils.py
import random


class outil(object):
   
    @classmethod
    def randomize(cls,
                  start,
                  final):
        return random \
            .randint(start, final)
            
pays={1:"Botwana",2:"Zambia",3:"Zimbabwe",4:"Mozambica",5:"Tanzania",6:"Kenya",7:"Angola"}
pays_liste=[]
for pays_index in range(1,8):
    pays_rand=pays[outil.randomize(1,pays_index)]
    pays_liste.append(pays_rand)
    
print(pays_liste)