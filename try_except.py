import sys

try:
    with open('webapp') as file:
        file_data = file.read()
    print(file_data)
except FileNotFoundError:
    print('Arquivo nao encontrado.')
except PermissionError:
    print('Sem permissao para visualizar/editar arquivo.')
except Exception as erro:
    print('Erro nao tratado.', str(erro))

