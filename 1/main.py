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
        name =  re.match(r'(\w+\s*(\w+\s*)*\b)',line).group()
        entity = re.search(r'ent_\w*',line).group()
        result.append((name, entity))

    result.sort(key=lambda x: unidecode.unidecode(x[0].casefold()))
    print("*** Utilizadores - Entidades ***")
    for r in result:
        print(r[0], "-", r[1])


#Produz uma lista ordenada alfabeticamente das entidades referenciadas, indicando, para cada uma, quantos
#utilizadores estão registados;

def entity_num_elements_list():
    entities = {}
    for line in text:
        entity = re.search(r'ent_\w*', line)
        if entity.group() not in entities:
            entities[entity.group()] = 1
        else:
            entities[entity.group()] +=1

    result = list(entities.items())
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

#Por fim, produz os seguintes indicadores:

#1. Quantos utilizadores?
#2. Quantas entidades?
#3. Qual a distribuição em número por entidade?
#4. Qual a distribuição em número por nível?

def indicators():
    users = set()
    entities = {}
    levels = {}
    for line in text:
        broken_line = re.split(r'::', line)
        users.add(re.match(r'(\w+\s*(\w+\s*)*\b)',broken_line[0]).group())
        entity = re.search(r'ent_\w*', broken_line[2]).group()
        level = re.search(r'\d+\.?\d*', broken_line[3]).group()

        if entity not in entities:
            entities[entity] = 1
        else:
            entities[entity] += 1
        if level not in levels:
            levels[level] = 1
        else:
            levels[level] += 1

    print("*** Indicadores ***")
    print(len(users), "Utilizadores")
    print(len(entities.keys()), "Entidades")
    print("")

    print("Distribuição de utilizadores por entidade:")
    for entity in sorted(entities.keys()):
        print(f"* {entity} - {entities[entity]}")
    print("")
    print("Distribuição de utilizadores por nivel:")
    for level in sorted(levels.keys()):
        print(f"* {level} - {levels[level]}")

#Para terminar, deve imprimir os 20 primeiros registos num novo cheiro de output mas em formato.

def json_20():
    return 0





def menu():
    cls = lambda: print('\n' * 50)
    inputfromuser = ""
    options = []
    options.append("Listagem com o nome e a entidade do utilizador, ordenada alfabeticamente por nome.")
    options.append("Lista ordenada alfabeticamente das entidades referenciadas, indicando, para cada uma, quantos utilizadores estão registados.")
    options.append("Distribuição de utilizadores por níveis de acesso.")
    options.append("Utilizadores, agrupados por entidade, ordenada primeiro pela entidade e dentro desta pelo nome.")
    options.append("Mostrar alguns indicadores.")
    options.append("Imprimir os 20 primeiros registos num novo ficheiro de output mas em formato jason")

    while inputfromuser != '0':
        print("***Selecione Opção***")
        for i in range(len(options)):
            print(f"{i+1} {options[i]}")
        print("0 Sair.")

        inputfromuser = input(">> ")
        while int(inputfromuser) > len(options) or int(inputfromuser) < 0:
            print("Opçao Invalida")
            inputfromuser = input(">> ")

        if inputfromuser == '0':
            continue
        elif inputfromuser == '1':
            name_entity_list()
        elif inputfromuser == '2':
            entity_num_elements_list()
        elif inputfromuser == '3':
            dist_users_level()
        elif inputfromuser == '4':
            name_entity_group()
        elif inputfromuser == '5':
            indicators()
        else:
            json_20()

        input("\nPressione Enter ")
        cls()



menu()
