import re
from typing import List 

with open('/home/gomes/Desktop/PLC/Trabalho/clav-users.txt', 'r') as f: 
    inputline_raw = f.readlines()
    list = []
    entity_dict = {}
    entity_list_temp = []

    for line in inputline_raw:
        print(line)
        print()
        param_line = re.split(r': ',line)
        name = re.search(r'^([A-Z][a-z]+\s)((([A-Z][a-z]+|(de)|(da)|(do)))\s)+:', line)
        entity = re.search(r'ent_[A-Za-z0-9]+(-\w+)?',line)
        
        entity_list_temp.append(entity.group())

        if name != None and entity != None:
            # Lista(nome,entidade) ordenada por entidade
            list.append((name.group()[:-2],entity.group()))
            list.sort()

            #Lista(entidade, nº usetilizadores) ordenada por entidade 


    for x in entity_list_temp:
        if x in entity_dict:
            entity_dict[x] = entity_dict[x]+1
        else: 
            entity_dict[x]=1

    for ent in sorted(entity_dict.items()):
        print(ent)
    
    


    print()
    for x in list:
        print(x)



#entidades = re.findall(r'ent_[A-Za-z0-9]+(-\w+)?', inputline_raw)



#print()
#print(nomes)
#print()
#print(entidades)

#^([A-Z][a-z]+\s)((([A-Z][a-z]+|(de)|(da)|(do)))\s)+:
    