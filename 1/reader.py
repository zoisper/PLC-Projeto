import re
import _json
from typing import List 

with open('clav-users.txt', 'r') as f:
    inputline_raw = f.readlines()
    name_dict = {}
    entity_list_temp = []
    level_dic = {}
    entity_dict = {}
    final_dict = {}


    for line in inputline_raw:

        param_line = re.split(r': ',line)
        name = re.search(r'^([A-Z][a-z]+\s)((([A-Z][a-z]+|(de)|(da)|(do)))\s)+:', line)
        print(name)
        entity = re.search(r'ent_[A-Za-z0-9]+(-\w+)?',line)
        level = re.search(r': \d :', line)
        
        entity_list_temp.append(entity.group())

        if name != None and entity != None:
            # Lista(nome,entidade) ordenada por entidade
            name_dict[name.group()[:-2]] = entity.group()

            #Lista de nivel 
            lvl = level.group()[2:][:-2]
            if lvl in level_dic.keys():
                level_dic[lvl]+=1
            else: 
                level_dic[lvl] = 1
            

#Lista(entidade, nº usetilizadores) ordenada por entidade 

    for x in entity_list_temp:
        if x in entity_dict:
            entity_dict[x] = entity_dict[x]+1
        else: 
            entity_dict[x]=1

    print("\nTeste\n")
    for entity in entity_dict.keys():
        for key,value in name_dict.items():
            if value == entity:
                if entity in final_dict.keys():
                    final_dict[entity].append(key)
                else:
                    final_dict[entity] = [key] 

    print("Numero de usuarios: ", len(name_dict.keys()))
    print()
    print("Numero de entitidades: ", len(entity_dict.keys()))
    print()
    
    for ent in final_dict.keys(): 
        print("Entidade: ", ent, " contem ", len(final_dict[ent]), " usuarios.")

    print()

    for lvl in level_dic.keys():
        print("O nivel ", lvl, " tem ", level_dic[lvl], " usuarios.")

#Json output
