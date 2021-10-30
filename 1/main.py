import re
import unidecode

'''Construa agora um ou vários programas
para processar o texto ' clav-users.txt ' em que campos de informação
têm a seguinte ordem: nome, email, entidade, nível, número de chamadas ao backend, com o intuito de calcular alguns
resultados conforme solicitado a seguir:'''


fp = open('clav-users.txt', 'r')
text = fp.readlines()

# Produz uma listagem apenas com o nome e a entidade do utilizador, ordenada alfabeticamente por nome;

def name_entity_list():
    result = []
    for line in text:
        name =  re.match(r'(^\w+\s*(\w+\s*)*\b)',line).group()
        entity = re.search(r'ent_\w*',line).group()
        result.append((name, entity))

    result.sort(key=lambda x: unidecode.unidecode(x[0].casefold()))
    print("*** Utilizadores - Entidades ***")
    for r in result:
        print(r[0], "-", r[1])


#Produz uma lista ordenada alfabeticamente das entidades referenciadas, indicando, para cada uma, quantos
#utilizadores estão registados;

def entity_num_elements_list():
    result = {}
    for line in text:
        entity = re.search(r'ent_\w*', line)
        if entity.group() not in result:
            result[entity.group()] = 1
        else:
            result[entity.group()] +=1

    result = list(result.items())
    result.sort()
    print("*** Entidades - Nº Utilizadores  ***")
    for r in result:
        print(r[0], "-", r[1])

#Qual a distribuição de utilizadores por níveis de acesso?

def dist_users_level():
    levels = {}
    for line in text:
        broken_line = re.split(r'::', line)
        level = re.search(r'\d+\.?\d*',broken_line[3]).group()
        if level not in levels:
            levels[level] = 1
        else:
            levels[level] += 1
    result = list(levels.items())
    result.sort()
    total_users = sum(x[1] for x in result )
    print("*** Nivel de Acesso - Distribuição  ***")
    for r in result:
        print(f"{r[0]} - {round((r[1]/total_users)*100,2)}%" )

#Produz uma listagem dos utilizadores, agrupados por entidade, ordenada primeiro pela entidade e dentro desta
#pelo nome;

def name_entity_group():
    result = {}
    for line in text:
        name = re.match(r'(^\w+\s*(\w+\s*)*\b)', line).group()
        entity = re.search(r'ent_\w*', line).group()
        if entity not in result:
            result[entity] = [name]
        else:
            result[entity].append(name)

    entities = list(result.keys())
    entities.sort()
    print("*** Utilizadores agrupados por entidade  ***")
    for entity in entities:
        print(f"{entity}:")
        result[entity].sort(key=lambda x: unidecode.unidecode(x.casefold()))
        for user in result[entity]:
            print("*",user)
        print("")







#name_entity_list()
#print("")
#entity_num_elements_list()
#print("")
#dist_users_level()
#name_entity_group()

