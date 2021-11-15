import re
import unidecode
import sys
import os.path


'''Construa agora um ou vários programas
para processar o texto ' clav-users.txt ' em que campos de informação
têm a seguinte ordem: nome, email, entidade, nível, número de chamadas ao backend, com o intuito de calcular alguns
resultados conforme solicitado a seguir:'''


# Produz uma listagem apenas com o nome e a entidade do utilizador, ordenada alfabeticamente por nome;

def name_entity_list():
    result = {}
    for line in text:
        user =  re.match(user_er,line).group()
        entity = re.search(entity_er,line).group()
        if user not in result:
            result[user] = [entity]
        else:
            result[user].append(', ')
            result[user].append(entity)
    result = list(result.items())
    result.sort(key=lambda x: unidecode.unidecode(x[0].casefold()))
    print("\n*** Utilizador : Entidade(s) ***\n")
    for r in result:
        print(r[0], ":", "".join(r[1]))


#Produz uma lista ordenada alfabeticamente das entidades referenciadas, indicando, para cada uma, quantos
#utilizadores estão registados;

def entity_num_elements_list():
    entities = {}
    for line in text:
        entity = re.search(entity_er, line).group()
        if entity not in entities:
            entities[entity] = 1
        else:
            entities[entity] +=1

    result = list(entities.items())
    result.sort()
    print("\n*** Entidade : Nº Utilizadores ***\n")
    for r in result:
        print(r[0], ":", r[1])

#Qual a distribuição de utilizadores por níveis de acesso?

def dist_users_level():
    levels = {}
    users = set()
    for line in text:
        broken_line = re.split(separator_er, line)
        user = re.match(user_er, broken_line[0]).group()
        level = re.search(level_er,broken_line[3]).group()
        if level not in levels:
            levels[level] = set()
            levels[level].add(user)
        else:
            levels[level].add(user)
        users.add(user)
    result = list(levels.items())
    result.sort()
    total_users = len(users)
    print("\n*** Nível de Acesso : Distribuição ***\n")
    for r in result:
        print(f"Nível {r[0]} : {round((len(r[1])/total_users)*100)}%" )
        for user in sorted(r[1], key=lambda x: unidecode.unidecode(x.casefold())):
            print("*",user)
        if(result.index(r) != len(result)-1):
            print("")


#Produz uma listagem dos utilizadores, agrupados por entidade, ordenada primeiro pela entidade e dentro desta
#pelo nome;

def name_entity_group():
    result = {}
    for line in text:
        user = re.match(user_er, line).group()
        entity = re.search(entity_er, line).group()
        if entity not in result:
            result[entity] = [user]
        else:
            result[entity].append(user)

    entities = list(result.keys())
    entities.sort()
    print("\n*** Utilizadores agrupados por entidade ***\n")
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
        broken_line = re.split(r'[:,|]+', line)
        users.add(re.match(user_er,broken_line[0]).group())
        entity = re.search(entity_er, broken_line[2]).group()
        level = re.search(level_er, broken_line[3]).group()

        if entity not in entities:
            entities[entity] = 1
        else:
            entities[entity] += 1
        if level not in levels:
            levels[level] = 1
        else:
            levels[level] += 1

    print("\n*** Indicadores ***\n")
    print("Número de Utilizadores:",len(users))
    print("")
    print("Número de Entidades:",len(entities.keys()))
    print("")
    print("Distribuição de utilizadores por entidade:")
    for entity in sorted(entities.keys()):
        print(f"* {entity} : {entities[entity]}")
    print("")
    print("Distribuição de utilizadores por nível:")
    for level in sorted(levels.keys()):
        print(f"* Nível {level} : {levels[level]}")

#Para terminar, deve imprimir os 20 primeiros registos num novo ficheiro de output mas em formato json.

def json_20():
    list = []
    N = len(text)
    if N >= 20:
        N = 20

    for i in range(N):
        broken_line = re.split(separator_er, text[i])
        user = re.match(user_er, broken_line[0]).group()
        email = re.search(email_er, broken_line[1]).group()
        entity = re.search(entity_er, broken_line[2]).group()
        level = re.search(level_er, broken_line[3]).group()
        calls = re.search(calls_er, broken_line[4]).group()
        list.append((user,email,entity,level,calls))

    file_name = input("\nDigite nome do ficheiro de output!\n>> ")
    fp = open(file_name, 'w')

    fp.write("{\n\t\"registos\":[\n")
    for i in range(len(list)):
        l = list[i]
        fp.write("\t\t{\n")
        fp.write(f"\t\t\t \"utilizador\":\"{l[0]}\",\n")
        fp.write(f"\t\t\t \"email\":\"{l[1]}\",\n")
        fp.write(f"\t\t\t \"entidade\":\"{l[2]}\",\n")
        fp.write(f"\t\t\t \"nível de acesso\":\"{l[3]}\",\n")
        fp.write(f"\t\t\t \"número de chamadas ao backend\":\"{l[4]}\"\n")
        if i != 19:
            fp.write("\t\t},\n")
        else:
            fp.write("\t\t}\n")
    fp.write("\t]\n}\n")
    fp.close()
    print(f"\nFicheiro \"{file_name}\" gerado com sucesso!")









def menu():
    cls = lambda: print('\n' * 50)
    inputfromuser = ""
    options = []
    options.append("Listagem com o nome e a entidade do utilizador, ordenada alfabeticamente por nome.")
    options.append("Lista ordenada alfabeticamente das entidades referenciadas, indicando, para cada uma, quantos utilizadores estão registados.")
    options.append("Distribuição de utilizadores por níveis de acesso.")
    options.append("Utilizadores, agrupados por entidade, ordenada primeiro pela entidade e dentro desta pelo nome.")
    options.append("Mostrar alguns indicadores.")
    options.append("Imprimir os 20 primeiros registos num novo ficheiro de output mas em formato jason.")
    cls()
    while inputfromuser != '0':
        print("*** Selecione Opção ***\n")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        print("0. Sair.")

        inputfromuser = input(">> ")
        while not inputfromuser.isdigit() or int(inputfromuser) > len(options) or int(inputfromuser) < 0:
            print("Opçao Invalida!")
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

        input("\nPressione Enter!\n>> ")
        cls()


if len(sys.argv)>1:
    text_source = sys.argv[1]
else:
    text_source = 'clav-users.txt'

if not os.path.exists(text_source):
    print(f"Ficheiro \"{text_source}\" não encontrado!")
    sys.exit(0)

fp = open(text_source, 'r')
text = fp.readlines()
fp.close()

calls_er = r'\d+'
entity_er = r'ent_\w*'
email_er = r'(\w+|\.|@|_|-)+'
level_er = r'\d+\.?\d*'
separator_er = r'[:,|]+'
user_er = r'(\w+\.?\s*(-?\w+\.?\s*)*\b)'

menu()

