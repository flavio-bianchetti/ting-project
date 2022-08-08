import sys
from ting_file_management.file_management import txt_importer


# https://www.geeksforgeeks.org/how-to-print-to-stderr-and-stdout-in-python/
def process(path_file, instance):
    inst = list()
    for index in range(0, len(instance)):
        inst.append(instance.search(index))

    if path_file not in inst:
        instance.enqueue(path_file)
        file = txt_importer(path_file)
        if file is not None:
            result = {
                'nome_do_arquivo': path_file,
                'qtd_linhas': len(file),
                'linhas_do_arquivo': file,
            }
            print(f'{result}', file=sys.stdout)


def remove(instance):
    if not len(instance):
        print('Não há elementos', file=sys.stdout)
        return

    result = instance.dequeue()

    print(f'Arquivo {result} removido com sucesso', file=sys.stdout)


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
