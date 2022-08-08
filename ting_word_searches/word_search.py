import sys
from ting_file_management.file_management import txt_importer


def exists_word(word, instance):
    inst = list()
    result = []
    for index in range(0, len(instance)):
        inst.append(instance.search(index))

    for item in inst:
        file = txt_importer(item)
        if file is not None:
            foundWordList = []
            for index, line in enumerate(file):
                if word.lower() in line.lower():
                    foundWordList.append({
                        'linha': index + 1
                    })
            if len(foundWordList):
                result.append({
                    'palavra': word,
                    'arquivo': item,
                    'ocorrencias': foundWordList,
                })
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
