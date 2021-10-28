import re 

with open('/home/gomes/Desktop/PLC/Trabalho/clav-users.txt', 'r') as f: 
    inputline_raw = f.readlines()
    list = []

    for line in inputline_raw:
        print(line)
        print()
        param_line = re.split(r': ',line)
        (name,entity) = re.search(r'^([A-Z][a-z]+\s)((([A-Z][a-z]+|(de)|(da)|(do)))\s)+:', line),re.search(r'ent_[A-Za-z0-9]+(-\w+)?',line)
        
        if name != None and entity != None:
            list.append((name.group()[:-2],entity.group()))
    
    for x in list:
        print(x)


#entidades = re.findall(r'ent_[A-Za-z0-9]+(-\w+)?', inputline_raw)



#print()
#print(nomes)
#print()
#print(entidades)

#^([A-Z][a-z]+\s)((([A-Z][a-z]+|(de)|(da)|(do)))\s)+:
    