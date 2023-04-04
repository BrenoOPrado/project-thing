import sys


def txt_importer(path_file):
    """Aqui irá sua implementação"""
    if '.txt' in path_file:
        try:
            with open(path_file, 'r') as file:
                data = file.read()
                informations = data.split('\n')
                return informations
        except FileNotFoundError:
            sys.stderr.write(f'Arquivo {path_file} não encontrado\n')
    else:
        sys.stderr.write('Formato inválido')
