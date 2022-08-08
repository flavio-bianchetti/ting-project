from ting_file_management.file_management import txt_importer


def create_output_words_found(path_file, word):
    file = txt_importer(path_file)
    if file is not None:
        foundWordList = []
        for index, line in enumerate(file):
            if word.lower() in line.lower():
                foundWordList.append({
                    'linha': index + 1
                })
        if len(foundWordList):
            return {
                'palavra': word,
                'arquivo': path_file,
                'ocorrencias': foundWordList,
            }
    return None


def exists_word(word, instance):
    inst = list()
    result = []
    for index in range(0, len(instance)):
        inst.append(instance.search(index))

    for path_file in inst:
        output_file = create_output_words_found(path_file, word)
        if output_file is not None:
            result.append(output_file)
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
