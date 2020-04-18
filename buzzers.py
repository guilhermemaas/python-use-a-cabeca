import csv
from datetime import datetime
import pprint

        
def convert2ampm(time24: str) -> str:
    return datetime.strptime(time24, '%H:%M').strftime('%I:%M%p')   

def print_divisor() ->str:
    print('=' * 30 + '\n')


with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
print_divisor()
pprint.pprint(flights)

print()

print_divisor()
flights2 = {}
for k, v in flights.items(): #k = key, v = value
    flights2[convert2ampm(k)] = v.title()
pprint.pprint(flights2)
print_divisor()
#in dic.items - Itera sobre os item do dicionario
#convert2ampm - converte a chave para o formato AM PM
#v.title() - Roda a o metodo title, converte a string para minusculo
#deixando a primeira letra como maiusculo
    
print_divisor()
flight_times = []
for ft in flights.keys():
    flight_times.append(convert2ampm(ft))
#Adiciona os horarios(chaves) de voos a uma nova lista
print(flight_times)
print_divisor()
flight_destinations = []
for fd in flights.values():
    flight_destinations.append(fd.title())
#Adiciona os locais de destino(valores) a uma nova lista
print(flight_destinations) 
print_divisor()

#Compreensao, para listas e for
more_dests = []
more_dests = [fd.title() for fd in flights.values()] #Itera a lista o dict flights, aplicando o title()
print(more_dests)
print_divisor()
flight_times2 = [convert2ampm(ft) for ft in flights.keys()]
print(flight_times2)
print_divisor()
#Compreensao, para dicionarios:
more_flights = {convert2ampm(key): value.title() for key, value in flights.items()}
print(more_flights) 

#Adicionando ifs nas compressoes
print_divisor()
just_freeport = {}
just_freeport = {convert2ampm(key): value.title() for key, value in flights.items() 
                 if value == 'FREEPORT'}
print(just_freeport)
just_freeport2 = {}
just_freeport2 = {convert2ampm(key): value.title()
                  for key, value in flights.items()
                  if value == 'FREEPORT'}
print(just_freeport2)

#Horarios por destino
print_divisor()
print('Horarios por destino:')
dest = set(more_flights.values())
print(dest)
print_divisor()
west_times = []
for key, value in more_flights.items():
    if value == 'West End':
        west_times.append(key)
print(f'West Times: {west_times}.')
west_times2 = [key for key, value in more_flights.items() if value == 'West End']
print(f'West Times2: {west_times2}.')
#Final
for dest in set(more_flights.values()):
    print(dest, '->', [key for key, value in more_flights.items() if value == dest])
#Adicionando a um dict
when = {}
for dest in set(more_flights.values()):
    when[dest] = [key for key, value in more_flights.items() if value == dest]
pprint.pprint(when)
print_divisor()
when2 = {dest: [key for key, value in more_flights.items() if value == dest] 
         for dest in set(more_flights.values())}
pprint.pprint(when2)

#Compreensao em Conjuntos
print_divisor()
vowels = {'a', 'e', 'i', 'o', 'u'}
message = "Don't forget to pack your towel."
found = set() #found = conjunto
for vowel in vowels:
    if vowel in message:
        found.add(vowel)
print(found)
found2 = {vowel for vowel in vowels if vowel in message}
print(found2)