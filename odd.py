from datetime import datetime, date
import time
#from datemite = modulo, import datetime = submodulo
#datetime fornece mecanismo para calcular o tempo

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57]

right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print('This minute seems a little odd.')
else:
    print('Not an odd minute')

print(date.today())
print(date.today().day)
print(date.today().month)
print(date.today().year)
print(date.isoformat(date.today()))

hora_atual = time.strftime('%H:%M')
dia_semana = time.strftime('%A %p')
print(hora_atual)
print(dia_semana)
