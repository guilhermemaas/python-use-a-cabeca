def myfunc(*args):
    for a in args:
        print(a, end='\n')
        print()
    if args:
        print()

#aceita qualquer lista de valores

def myfunc2(**kwargs):
    for k, v in kwargs.items():
        print(k, v, sep='->', end='.\n')
        print()
    if kwargs:
        print()

#aceita qualquer quantidade de pares chave/valor


def myfunc3(*args, **kwargs):
    for a in args:
        print(a, end='.\n')
        print()
    print('='*10)
    for k, v in kwargs.items():
        print(k, v, sep=' -> ', end='.\n')
        print()
"""
>>> mylist = [1, 'dois', 3, 'quatro', 5]
>>> mydic = {'1': 1, '2': 2, 'tres': 3, 'quatro': 4, 'cinco': 5}
>>> myfunc3(*mylist, **mydic)
1.

dois.

3.

quatro.

5.

==========
1 -> 1.

2 -> 2.

tres -> 3.

quatro -> 4.

cinco -> 5.
"""


        
