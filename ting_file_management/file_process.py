from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    """Aqui irá sua implementação"""
    wasntAdd = True

    if instance.__len__() > 0:
        for data in instance.seeData():
            if data['nome_do_arquivo'] == path_file:
                wasntAdd = False

    if wasntAdd:
        data = txt_importer(path_file)
        length = len(data)
        res = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": length,
            "linhas_do_arquivo": data
        }

        instance.enqueue(res)
        print(res)


def remove(instance):
    """Aqui irá sua implementação"""
    if instance.__len__() == 0:
        print('Não há elementos')
    else:
        data = instance.dequeue()
        print(f'Arquivo {data["nome_do_arquivo"]} removido com sucesso')


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
    if position < 0 or position >= instance.__len__():
        sys.stderr.write("Posição inválida")
    else:
        data = instance.search(position)
        print(data)
